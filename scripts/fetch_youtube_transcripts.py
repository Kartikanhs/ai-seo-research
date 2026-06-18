"""
fetch_youtube_transcripts.py

Pulls transcripts for a list of YouTube videos and saves each one as a
markdown file with metadata frontmatter, organized into:
    research/youtube-transcripts/<author-slug>/<date>-<title-slug>-<video_id>.md

Two collection methods are supported:

1. youtube-transcript-api  (free, no API key)
   pip install youtube-transcript-api --break-system-packages
   Note: YouTube frequently blocks requests coming from datacenter/cloud IPs
   (AWS, GCP, most CI runners). This works reliably from a home/office
   connection but may fail from Claude Code's sandboxed environment, a
   GitHub Actions runner, etc. If you hit repeated "IP blocked" or
   "no transcript available" errors, switch to Supadata.

2. Supadata API (https://supadata.ai) (free tier available, paid above that)
   Works reliably from servers since it's a hosted service, not a scraper
   running on your own IP. Get an API key, then:
   python fetch_youtube_transcripts.py --method supadata --api-key YOUR_KEY

Usage:
    python fetch_youtube_transcripts.py --method youtube-transcript-api
    python fetch_youtube_transcripts.py --method supadata --api-key sk_...

Input file: scripts/video_list.csv
    columns: author,title,url,published   (published is optional, YYYY-MM-DD)
"""

import argparse
import csv
import json
import os
import re
import sys
import time
from pathlib import Path
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT / "research" / "youtube-transcripts"
DEFAULT_VIDEO_LIST = Path(__file__).resolve().parent / "video_list.csv"


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:80] or "untitled"


def extract_video_id(url_or_id: str) -> str:
    url_or_id = url_or_id.strip()
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", url_or_id):
        return url_or_id
    match = re.search(r"(?:v=|youtu\.be/|shorts/)([A-Za-z0-9_-]{11})", url_or_id)
    if match:
        return match.group(1)
    raise ValueError(f"Could not extract an 11-character video ID from: {url_or_id}")


def fetch_with_youtube_transcript_api(video_id: str) -> str:
    from youtube_transcript_api import YouTubeTranscriptApi

    # The library changed its API in v1.0: the old interface was a
    # classmethod YouTubeTranscriptApi.get_transcript(video_id); the
    # current interface is instance-based: YouTubeTranscriptApi().fetch(video_id).
    # Support both so this script doesn't silently break on a version bump.
    if hasattr(YouTubeTranscriptApi, "get_transcript"):
        raw = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join(chunk["text"].strip() for chunk in raw if chunk["text"].strip())

    fetched = YouTubeTranscriptApi().fetch(video_id)
    return " ".join(snippet.text.strip() for snippet in fetched if snippet.text.strip())


def fetch_with_supadata(video_id: str, api_key: str) -> str:
    import requests

    resp = requests.get(
        "https://api.supadata.ai/v1/youtube/transcript",
        params={"videoId": video_id, "text": "true"},
        headers={"x-api-key": api_key},
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    # Supadata's response shape has shifted between versions; handle both.
    return data.get("content") or data.get("transcript") or json.dumps(data, indent=2)


def save_transcript(author: str, title: str, video_id: str, url: str, published: str, text: str) -> Path:
    author_dir = OUTPUT_DIR / slugify(author)
    author_dir.mkdir(parents=True, exist_ok=True)

    date_prefix = published if published else "undated"
    filename = f"{date_prefix}-{slugify(title)}-{video_id}.md"
    filepath = author_dir / filename

    frontmatter = (
        "---\n"
        f"author: {author}\n"
        f'title: "{title}"\n'
        f"video_id: {video_id}\n"
        f"url: {url}\n"
        f"published: {published or 'unknown'}\n"
        f"collected_on: {datetime.now(timezone.utc).date().isoformat()}\n"
        "---\n\n"
    )

    filepath.write_text(frontmatter + text + "\n", encoding="utf-8")
    return filepath


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--method",
        choices=["youtube-transcript-api", "supadata"],
        default="youtube-transcript-api",
        help="Which transcript source to use.",
    )
    parser.add_argument(
        "--api-key",
        default=os.environ.get("SUPADATA_API_KEY"),
        help="Supadata API key (or set SUPADATA_API_KEY env var). Required for --method supadata.",
    )
    parser.add_argument(
        "--video-list",
        default=str(DEFAULT_VIDEO_LIST),
        help="Path to the CSV file listing videos to fetch.",
    )
    args = parser.parse_args()

    video_list_path = Path(args.video_list)
    if not video_list_path.exists():
        sys.exit(f"Video list not found: {video_list_path}\nFill in scripts/video_list.csv first.")

    with open(video_list_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if not rows:
        sys.exit("video_list.csv has no rows. Add at least one video per expert.")

    print(f"Found {len(rows)} videos to fetch using method: {args.method}\n")

    ok, failed = 0, 0
    for i, row in enumerate(rows, start=1):
        author = (row.get("author") or "").strip()
        title = (row.get("title") or "").strip()
        url = (row.get("url") or "").strip()
        published = (row.get("published") or "").strip()

        if not author or not url:
            print(f"[{i}/{len(rows)}] SKIPPED — row missing author or url: {row}")
            failed += 1
            continue

        try:
            video_id = extract_video_id(url)
            print(f"[{i}/{len(rows)}] {author} — {title or video_id}")

            if args.method == "youtube-transcript-api":
                text = fetch_with_youtube_transcript_api(video_id)
            else:
                if not args.api_key:
                    sys.exit("Supadata method requires --api-key or SUPADATA_API_KEY env var.")
                text = fetch_with_supadata(video_id, args.api_key)

            path = save_transcript(author, title or video_id, video_id, url, published, text)
            print(f"    saved -> {path.relative_to(REPO_ROOT)}")
            ok += 1

        except Exception as e:
            print(f"    FAILED: {e}")
            failed += 1

        time.sleep(1)  # be polite, avoid hammering the API

    print(f"\nDone. {ok} succeeded, {failed} failed.")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
