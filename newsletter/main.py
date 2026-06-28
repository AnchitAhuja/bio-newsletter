"""
main.py — orchestrates the full pipeline

Usage:
  python main.py          → Run now, send email
  python main.py --test   → Dry run, print briefing only
  python main.py --schedule → Run every Sunday 8am IST
"""

import os
import sys
import argparse
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

import schedule
import time

from fetcher import fetch_all_feeds, format_articles_for_claude
from analyst import run_analysis, add_header_footer
from sender import send_email
from config import NEWSLETTER


def run_newsletter(dry_run: bool = False):
    print(f"\n{'='*50}")
    print(f"🚀 Before It's Obvious — Newsletter Pipeline")
    print(f"   {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}")

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    sender_email = os.environ.get("GMAIL_SENDER")
    sender_password = os.environ.get("GMAIL_APP_PASSWORD")
    recipient_email = os.environ.get("GMAIL_RECIPIENT")

    if not api_key:
        print("✗ Missing ANTHROPIC_API_KEY in .env")
        sys.exit(1)
    if not dry_run and not all([sender_email, sender_password, recipient_email]):
        print("✗ Missing Gmail vars in .env (GMAIL_SENDER, GMAIL_APP_PASSWORD, GMAIL_RECIPIENT)")
        sys.exit(1)

    # Step 1: Fetch
    articles = fetch_all_feeds()

    # Step 2: Format
    articles_text = format_articles_for_claude(articles)

    # Step 3: Analyse
    briefing = run_analysis(articles_text, api_key)
    full_briefing = add_header_footer(briefing)

    # Step 4: Output
    if dry_run:
        print("\n" + "="*50)
        print("DRY RUN — briefing preview:")
        print("="*50)
        print(full_briefing)
        print("\n✓ Dry run complete. No email sent.")
    else:
        send_email(
            briefing=full_briefing,
            sender_email=sender_email,
            sender_app_password=sender_password,
            recipient_email=recipient_email,
            subject_template=NEWSLETTER["subject"],
        )
        print("\n✅ Done.")


def run_on_schedule():
    print("⏰ Scheduler running — fires every Sunday at 08:00 IST")
    print("   Press Ctrl+C to stop\n")

    # Run once immediately on startup to verify
    print("Running once now to verify setup...")
    run_newsletter()

    schedule.every().sunday.at("08:00").do(run_newsletter)

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--schedule", action="store_true", help="Run on weekly schedule")
    parser.add_argument("--test", action="store_true", help="Dry run — print, don't send")
    args = parser.parse_args()

    if args.schedule:
        run_on_schedule()
    elif args.test:
        run_newsletter(dry_run=True)
    else:
        run_newsletter(dry_run=False)
