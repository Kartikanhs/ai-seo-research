# AI-Powered SEO Content Production — Research Repo

A research project dedicated to collecting and organizing content from 10 elite practitioners of AI-powered SEO content production, serving as the foundation for a future playbook.

## Why this topic

AI-powered SEO content production was chosen because it has an unusually wide gap between genuine practitioners (people sharing real traffic data, cost-per-article numbers, and reproducible workflows) and generic "10 AI SEO tips" content. That gap makes expert selection a meaningful judgment call rather than a Google-the-top-10-results exercise.

## Who's in here and why

See [`research/sources.md`](research/sources.md) for the full list with links and annotations. In short: a mix of independent newsletter writers (Kevin Indig, Glen Allsopp), agency operators sharing client data (Steve Toth, Mike King, Charles Floate), platform-side researchers running large-scale studies (Ryan Law at Ahrefs, Patrick Stox formerly at Ahrefs), and consultants translating client work into public frameworks (Aleyda Solis, Eli Schwartz, Authority Hacker). The goal was range across how AI-SEO content production actually gets practiced, not 10 people doing the same thing.

One entry carries a caveat worth knowing before relying on it in a playbook: Charles Floate's tactics lean black-hat/aggressive (see his source notes for detail).

## Repo structure

```
research/
  sources.md                 — the 10 experts, links, dates found, why they qualify
  youtube-transcripts/
    <author-slug>/<date>-<title-slug>-<video_id>.md
  linkedin-posts/
    <author-slug>/<date>-<topic-slug>.md
  other/                      — any extra materials (articles, slide decks, etc.)
scripts/
  fetch_youtube_transcripts.py  — pulls transcripts via API
  add_linkedin_post.py          — semi-manual LinkedIn post collector
  generate_analysis.py          — generates the summary report in research/other/
  video_list.csv                 — config: which videos to fetch transcripts for
```
## How content was collected

**YouTube transcripts** — pulled via API using `scripts/fetch_youtube_transcripts.py`. Two methods are supported:
- `youtube-transcript-api` (free, no key) — works well from a normal internet connection, but YouTube often blocks requests from cloud/CI IPs, and some videos have subtitles disabled entirely.
- [Supadata](https://supadata.ai/) API (free tier, then paid) — more reliable from servers since it's a hosted service rather than a scraper running on your own IP.

**LinkedIn posts** — LinkedIn has no public API for reading another user's posts and actively blocks scraping, so these were collected semi-manually: copy the post text and permalink from the platform, then run `scripts/add_linkedin_post.py` to save it with consistent structure and metadata instead of free-form copy-pasting.

## Running the scripts

```bash
pip3 install -r requirements.txt --break-system-packages   # if needed on your system

# Fetch YouTube transcripts (edit scripts/video_list.csv first)
python3 scripts/fetch_youtube_transcripts.py --method youtube-transcript-api
# or, if the free method gets IP-blocked or subtitles are disabled:
python3 scripts/fetch_youtube_transcripts.py --method supadata --api-key YOUR_KEY

# Add a LinkedIn post (interactive)
python3 scripts/add_linkedin_post.py
```

## Commit history

Commits were made incrementally as sources were identified and content was collected, rather than as a single end-of-project dump — see the commit log for the actual research timeline.
