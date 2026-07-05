"""
analyst.py — sends articles to Claude, gets structured briefing
"""

import anthropic
from datetime import datetime
from config import PORTFOLIO, WATCHLIST, BULLISH_SIGNALS, BEARISH_SIGNALS


def build_prompt(articles_text: str) -> tuple[str, str]:
    portfolio_lines = []
    for ticker, d in PORTFOLIO.items():
        drivers = ", ".join(d["thesis_drivers"])
        portfolio_lines.append(f"- {ticker} ({d.get('name', ticker)}): {d['thesis']}\n  Watch for: {drivers}")

    watchlist_lines = []
    for ticker, d in WATCHLIST.items():
        drivers = ", ".join(d["thesis_drivers"])
        watchlist_lines.append(f"- {ticker}: {d['thesis']}\n  Watch for: {drivers}")

    bull = ", ".join(f'"{s}"' for s in BULLISH_SIGNALS[:10])
    bear = ", ".join(f'"{s}"' for s in BEARISH_SIGNALS[:8])

    system = f"""You are a personal investment analyst for Anchit, a retail investor based in India.

His investment philosophy:
- AI value chain thesis: Energy → Chips → AI Platforms → AI Adopters
- Long-term (5-10 year) horizon, buys and holds
- 6-month thesis reviews only — not daily monitoring
- Only takes risks he can research — geopolitics is a hard no
- "Reuters writing an explainer = trade is late" — signal is in earnings calls, supply agreements, TrendForce data

Portfolio (what to monitor):
{chr(10).join(portfolio_lines)}

Watchlist (potential buys):
{chr(10).join(watchlist_lines)}

High-priority signal words:
BULLISH: {bull}
BEARISH: {bear}

Produce this exact output structure:

---THESIS CHECK---
One line per position: [TICKER] — [INTACT/WATCH/WEAKENING] — [reason or "No relevant news this week"]

---SIGNALS THIS WEEK---
Only articles containing signal words or directly affecting thesis drivers.
Format: [SOURCE] [DATE] — [TITLE] — [Why it matters + which position] — [URL]
Max 8 items. If nothing: "No significant signals this week."

---WATCHLIST ALERTS---
News affecting NOW, PLTR, SNDK, MOD or other watchlist names.
Include entry timing observations if relevant.
If nothing: "No watchlist updates this week."

---UNEXPECTED CONNECTIONS---
This is the most important section. Look for:
- Any company in the portfolio partnering with or acquiring another portfolio/watchlist company
- Supply chain relationships tightening between two watched companies
- A CEO from one watched company endorsing or visiting another
- Any signal that creates overlap between two stages of the AI value chain
- The Anthropic-ServiceNow type signal: where two things Anchit already tracks connect in a new way
If nothing found: "No unexpected connections this week."

---NEW OPPORTUNITY RADAR---
Any article suggesting a NEW structural shift, supply constraint, or M&A pattern NOT already in portfolio.
This is the "what are we missing" section.
Max 3 items. If nothing: "Nothing new on radar this week."

---STRATECHERY REMINDER---
Always include: "📖 Read Stratechery this week: stratechery.com — 15 min long read"

Target reading time: 10-15 minutes. Depth over brevity.

For every signal and thesis check:
- Name the company and explain in one sentence what it actually does (assume reader knows the thesis but not every company name)
- Explain WHY this news matters — not just what happened, but the cause-effect chain
- Quantify where possible — numbers beat adjectives
- If a signal is bullish, say exactly how it strengthens the thesis
- If a signal is bearish, say exactly what would have to be true for it to break the thesis

For Unexpected Connections: go deeper. Explain the full chain — why these two things connecting matters more than either alone.

For New Opportunity Radar: give enough context that the reader can evaluate whether to research further — what the company does, why it might be the next bottleneck, what the early signal is.

Be direct. No hedging. No disclaimers. If uncertain, say "Unclear."
"""

    user = f"""Analyse this week's articles and produce the briefing.

{articles_text}

Today: {datetime.now().strftime("%B %d, %Y")}
"""
    return system, user


def run_analysis(articles_text: str, api_key: str) -> str:
    client = anthropic.Anthropic(api_key=api_key)
    system, user = build_prompt(articles_text)

    print("\n🤖 Sending to Claude for analysis...")

    try:
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=4000,
            system=system,
            messages=[{"role": "user", "content": user}]
        )
        briefing = message.content[0].text
        print(f"✓ Done ({message.usage.input_tokens} in / {message.usage.output_tokens} out tokens)")
        return briefing

    except Exception as e:
        print(f"✗ Claude API error: {e}")
        return f"ERROR: Could not generate analysis — {e}"


def add_header_footer(briefing: str) -> str:
    date_str = datetime.now().strftime("%B %d, %Y")
    header = f"""BEFORE IT'S OBVIOUS — WEEKLY BRIEFING
{date_str}
{'='*50}

"""
    footer = f"""
{'='*50}
Sources: TrendForce, Reuters, Seeking Alpha, Google Alerts
Not financial advice — personal research digest.
"""
    return header + briefing + footer
