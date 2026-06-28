"""
fetcher.py — pulls articles from RSS feeds
"""

import feedparser
import httpx
import re
import time
from datetime import datetime, timedelta, timezone
from typing import Optional
from config import RSS_FEEDS, GOOGLE_ALERT_FEEDS, NEWSLETTER


def fetch_feed(url: str, name: str, lookback_days: int) -> list[dict]:
    articles = []
    cutoff = datetime.now(timezone.utc) - timedelta(days=lookback_days)

    try:
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}
        response = httpx.get(url, headers=headers, timeout=15, follow_redirects=True)
        feed = feedparser.parse(response.text)

        for entry in feed.entries:
            pub_date = None
            if hasattr(entry, "published_parsed") and entry.published_parsed:
                pub_date = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
            elif hasattr(entry, "updated_parsed") and entry.updated_parsed:
                pub_date = datetime(*entry.updated_parsed[:6], tzinfo=timezone.utc)

            if pub_date and pub_date < cutoff:
                continue

            summary = ""
            if hasattr(entry, "summary"):
                summary = re.sub(r"<[^>]+>", "", entry.summary).strip()[:500]

            articles.append({
                "source": name,
                "title": entry.get("title", "").strip(),
                "summary": summary,
                "url": entry.get("link", ""),
                "published": pub_date.strftime("%Y-%m-%d") if pub_date else "unknown",
            })

        print(f"  ✓ {name}: {len(articles)} articles")

    except Exception as e:
        print(f"  ✗ {name}: Failed — {e}")

    return articles


def fetch_all_feeds(lookback_days: Optional[int] = None) -> list[dict]:
    if lookback_days is None:
        lookback_days = NEWSLETTER["lookback_days"]

    all_articles = []
    max_per = NEWSLETTER["max_items_per_source"]

    print("\n📡 Fetching feeds...")

    all_feeds = RSS_FEEDS + [
        {"name": "Google Alert", "url": url, "type": "alert", "description": "Google Alert"}
        for url in GOOGLE_ALERT_FEEDS
    ]

    for feed in all_feeds:
        articles = fetch_feed(feed["url"], feed["name"], lookback_days)
        for a in articles[:max_per]:
            a["feed_type"] = feed.get("type", "general")
            all_articles.append(a)
        time.sleep(0.5)

    print(f"\n📰 Total articles fetched: {len(all_articles)}")
    return all_articles


def format_articles_for_claude(articles: list[dict]) -> str:
    if not articles:
        return "No articles fetched this week."

    lines = []
    for i, a in enumerate(articles, 1):
        lines.append(f"[{i}] SOURCE: {a['source']} | DATE: {a['published']}")
        lines.append(f"TITLE: {a['title']}")
        if a.get("summary"):
            lines.append(f"SUMMARY: {a['summary']}")
        lines.append(f"URL: {a['url']}")
        lines.append("")

    return "\n".join(lines)
