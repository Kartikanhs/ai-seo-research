"""
add_linkedin_post.py

LinkedIn has no public API for reading another user's posts, and automated
scraping violates its Terms of Service and gets IPs/accounts blocked
quickly (this is true even with most "LinkedIn scraper" tools — they work
until they don't). The realistic approach for a project like this is
semi-manual collection: open the expert's profile, copy a post's text and
permalink, and run this script to save it with consistent structure and
metadata instead of pasting ad hoc files by hand.

Usage:
    python add_linkedin_post.py

It will prompt you for:
    - author name
    - post date (as shown on LinkedIn)
    - post URL (permalink — click the post's timestamp to get this)
    - a short topic/title (used only for the filename)
    - the post text itself (paste it, then type END on its own line)
    - an optional one-line note on why it's relevant

Output:
    research/linkedin-posts/<author-slug>/<date>-<topic-slug>.md
"""

import re
import sys
from pathlib import Path
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT / "research" / "linkedin-posts"


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:60] or "untitled"


def prompt(label: str) -> str:
    return input(f"{label}: ").strip()


def read_multiline_body() -> str:
    print("Paste the post text below. End with a line containing only END:")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines).strip()


def main():
    print("=== Add a LinkedIn post to the research repo ===\n")

    author = prompt("Author name")
    if not author:
        sys.exit("Author name is required.")

    post_date = prompt("Post date (YYYY-MM-DD, as shown on LinkedIn)")
    url = prompt("Post URL (permalink)")
    topic = prompt("Short topic/title (for the filename)")
    body = read_multiline_body()
    note = prompt("Optional: 1-line note on why this post is relevant")

    if not body:
        sys.exit("Post text cannot be empty.")

    author_dir = OUTPUT_DIR / slugify(author)
    author_dir.mkdir(parents=True, exist_ok=True)

    date_prefix = post_date if post_date else "undated"
    filename = f"{date_prefix}-{slugify(topic)}.md"
    filepath = author_dir / filename

    if filepath.exists():
        overwrite = prompt(f"{filepath.name} already exists — overwrite? (y/N)")
        if overwrite.lower() != "y":
            print("Aborted.")
            return

    content = (
        "---\n"
        f"author: {author}\n"
        f"date: {post_date or 'unknown'}\n"
        f"url: {url}\n"
        f"collected_on: {datetime.now(timezone.utc).date().isoformat()}\n"
        f'note: "{note}"\n'
        "---\n\n"
        f"{body}\n"
    )

    filepath.write_text(content, encoding="utf-8")
    print(f"\nSaved -> {filepath.relative_to(REPO_ROOT)}")
    print("Remember to commit: git add . && git commit -m \"Add LinkedIn post: " + author + "\"")


if __name__ == "__main__":
    main()
