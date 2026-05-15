"""
fetch_publications.py
Fetches publications from Google Scholar using the `scholarly` library
and writes them to publications.json in the repo root.

Required: set SCHOLAR_AUTHOR_ID as a repository variable in
  Settings → Secrets and variables → Actions → Variables
  The ID is the `user=` parameter from your Scholar profile URL, e.g.
  https://scholar.google.com/citations?user=XXXXXXXXXX
                                              ^^^^^^^^^^
"""

import json
import os
import sys
import time

from scholarly import scholarly, ProxyGenerator

AUTHOR_ID = os.environ.get("SCHOLAR_AUTHOR_ID", "1R0IoRMAAAAJ").strip()
OUTPUT = os.path.join(os.path.dirname(__file__), "..", "publications.json")

if not AUTHOR_ID:
    print("ERROR: SCHOLAR_AUTHOR_ID environment variable is not set.", file=sys.stderr)
    sys.exit(1)


def fetch(author_id: str) -> dict:
    print(f"Fetching Scholar profile for author ID: {author_id}")
    author = scholarly.search_author_id(author_id)
    author = scholarly.fill(author, sections=["basics", "publications"])

    name = author.get("name", "")
    scholar_url = f"https://scholar.google.com/citations?user={author_id}"

    pubs = []
    for i, pub in enumerate(author.get("publications", [])):
        bib = pub.get("bib", {})

        title = bib.get("title", "").strip()
        if not title:
            continue

        # Venue: prefer 'venue', then 'journal', then 'booktitle'
        venue = (
            bib.get("venue") or bib.get("journal") or bib.get("booktitle") or ""
        ).strip()

        authors = bib.get("author", "").strip()
        year = str(bib.get("pub_year", "")).strip()
        url = pub.get("pub_url", "")

        pubs.append(
            {
                "title": title,
                "authors": authors,
                "venue": venue,
                "year": year,
                "url": url,
            }
        )

        # Be polite — small pause every 10 publications
        if i > 0 and i % 10 == 0:
            time.sleep(2)

    # Sort newest first; put undated entries at the end
    pubs.sort(key=lambda p: p["year"] or "0", reverse=True)

    return {
        "author": name,
        "scholar_url": scholar_url,
        "publications": pubs,
    }


def main():
    data = fetch(AUTHOR_ID)
    out_path = os.path.abspath(OUTPUT)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(data['publications'])} publications → {out_path}")


if __name__ == "__main__":
    main()
