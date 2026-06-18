# Sources — AI-Powered SEO Content Production

10 practitioners selected for genuinely operating AI-powered SEO/content
systems (their own or clients'), not just publishing generic "AI + SEO"
listicle content. Each entry notes where their highest-signal content lives
and why they made the cut.

---

### 1. Kevin Indig
- **Role:** Organic growth advisor; ex-Head of SEO/Growth at Shopify, Atlassian, G2
- **Primary platform:** Newsletter — [Growth Memo](https://www.growth-memo.com/) (Substack, ~23k subscribers)
- **Secondary:** Co-hosts the *Contrarian Marketing* podcast with Eli Schwartz
- **Found via:** Web search, 2026-06-18
- **Why he qualifies:** Publishes recurring "Growth Intelligence Briefs" tracking AI search visibility across thousands of domains with real numbers, and has written about building his own internal tools to automate topic prioritization, SEO testing, and reporting for clients.

### 2. Glen Allsopp
- **Role:** Founder, Detailed.com; now also writes for Ahrefs
- **Primary platform:** Blog — [Detailed.com](https://detailed.com/) / [Ahrefs blog](https://ahrefs.com/blog/author/glen-allsopp/)
- **Found via:** Web search, 2026-06-18
- **Why he qualifies:** Does primary research rather than recycled takes — personally attends public-company earnings calls to track what they say about SEO and AI search, publishing the raw data.

### 3. Gael Breton & Mark Webster (Authority Hacker)
- **Role:** Co-founders, Authority Hacker
- **Primary platform:** YouTube/Podcast — [@AuthorityHackerPodcast](https://www.youtube.com/@AuthorityHackerPodcast)
- **Found via:** Web search, 2026-06-18
- **Why they qualify:** Podcast has pivoted explicitly to "real workflows, real results" — screen-recorded walkthroughs of the actual AI/automation systems they run in their own business, not just commentary.

### 4. Charles Floate
- **Role:** SEO entrepreneur, runs an AI-driven SEO agency
- **Primary platform:** YouTube interviews/podcasts; training site (charlesfloate.com)
- **Found via:** Web search, 2026-06-18
- **Why he qualifies:** Unusually transparent with operational numbers — cost-per-article, content quality scores, output volume.
- **Caveat:** Tactics lean black-hat/aggressive (parasite SEO, spam techniques). Real practitioner, but ethically gray — flag this if your playbook wants a "clean" source set.

### 5. Steve Toth
- **Role:** CEO, Notebook Agency; runs SEO Notebook / AI Notebook
- **Primary platform:** LinkedIn (very active) + webinars/podcasts
- **Found via:** Web search, 2026-06-18
- **Why he qualifies:** Posts client-numbers-backed content on AEO/AI search workflows; agency actively implements what he posts about.

### 6. Ryan Law
- **Role:** Director of Content Marketing, Ahrefs
- **Primary platform:** Ahrefs blog/podcast
- **Found via:** Web search, 2026-06-18
- **Why he qualifies:** Leads large-scale, data-driven studies on AI search/AEO (millions of data points) rather than publishing opinion pieces.

### 7. Patrick Stox
- **Role:** Product Advisor, Ahrefs
- **Primary platform:** Ahrefs blog/podcast
- **Found via:** Web search, 2026-06-18
- **Why he qualifies:** Known for skeptical, data-backed pushback on AEO hype — useful counterweight to more promotional voices.

### 8. Aleyda Solis
- **Role:** Founder, Orainti (international SEO consultancy)
- **Primary platform:** Newsletter — SEOFOMO / AI Marketers; YouTube — *Crawling Mondays*
- **Found via:** Web search, 2026-06-18
- **Why she qualifies:** Active consulting practitioner across ecommerce/SaaS clients; publishes a concrete "AI Search Optimization Roadmap" from that client work, not abstract theory.

### 9. Eli Schwartz
- **Role:** Growth advisor; author, *Product-Led SEO*
- **Primary platform:** Co-hosts *Contrarian Marketing* podcast; elischwartz.co
- **Found via:** Web search, 2026-06-18
- **Why he qualifies:** Distinct, testable thesis (product-led pages resist AI displacement) backed by his own advisory work with high-growth companies.

### 10. Mike King
- **Role:** Founder, iPullRank (technical SEO + AI search agency)
- **Primary platform:** Webinars/conferences; agency case studies
- **Found via:** Web search, 2026-06-18
- **Why he qualifies:** Agency practitioner building real AI/retrieval systems for clients.
- **Caveat:** Found via a secondary citation rather than a direct profile pull — verify his current LinkedIn/YouTube cadence before treating this as a final source.

---

## Notes on collection method
- **YouTube:** transcripts pulled via API (see `/scripts/fetch_youtube_transcripts.py`) — either the free `youtube-transcript-api` library or the Supadata API as a fallback.
- **LinkedIn:** LinkedIn has no public API and actively blocks scraping. Posts are collected semi-manually via `/scripts/add_linkedin_post.py`, which standardizes formatting and metadata but requires a human to copy text from the platform.
