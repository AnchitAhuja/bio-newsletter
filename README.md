# Before It's Obvious — Investment Newsletter

AI analyst that runs every Sunday, fetches news from your sources,
filters against your thesis, delivers a 10-minute briefing to your inbox.

---

## Mac Setup (15 minutes)

### Step 1 — Python (Mac already has it, but install a fresh one)

```bash
# Check if Python 3 is installed
python3 --version

# If not, install via Homebrew (recommended)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
```

### Step 2 — Create project folder and virtual environment

```bash
mkdir ~/newsletter
cd ~/newsletter
python3 -m venv venv
source venv/bin/activate
```

You'll see `(venv)` in your terminal — means it's active.

### Step 3 — Copy files into ~/newsletter/

Copy all 8 files into this folder:
- config.py
- fetcher.py
- analyst.py
- sender.py
- main.py
- requirements.txt
- railway.json
- .gitignore

### Step 4 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 5 — Create your .env file

```bash
cp .env.example .env
```

Edit `.env` with your values:
```
ANTHROPIC_API_KEY=     ← from console.anthropic.com/account/keys
GMAIL_SENDER=          ← Gmail you'll SEND FROM
GMAIL_APP_PASSWORD=    ← see below
GMAIL_RECIPIENT=       ← Gmail you'll SEND TO (can be same or different)
```

### Step 6 — Gmail App Password

You need an App Password (not your normal Gmail password).

1. Go to myaccount.google.com
2. Security → 2-Step Verification → App passwords
3. Create one named "Investment Newsletter"
4. Copy the 16-character password → paste into GMAIL_APP_PASSWORD in .env
5. Note: 2FA must be enabled on your Gmail

### Step 7 — Test it

```bash
# Make sure venv is active (you should see (venv) in terminal)
source venv/bin/activate

# Dry run — prints briefing, no email sent
python main.py --test

# Full run — sends actual email
python main.py
```

---

## Set Up Google Alerts (5 minutes, adds the best signals)

1. Go to google.com/alerts
2. Create alerts for:
   - "data center acquisition"
   - "HBM memory demand"
   - "semiconductor supply sold out"
   - "nuclear power data center"
   - "AI infrastructure capex"
   - "Jensen Huang"
3. For each: set Deliver to → RSS feed
4. Copy each RSS URL into GOOGLE_ALERT_FEEDS in config.py

---

## Deploy to Railway (always-on, fires even when laptop is closed)

### Step 1 — Push to GitHub

```bash
cd ~/newsletter
git init
git add .
git commit -m "initial setup"
# Create a repo on github.com, then:
git remote add origin https://github.com/YOUR_USERNAME/bio-newsletter
git push -u origin main
```

Make sure .env is in .gitignore — never push API keys.

### Step 2 — Deploy on Railway

1. Go to railway.app → sign up (free)
2. New Project → Deploy from GitHub repo
3. Select your repo
4. Go to Variables tab → add all 4 env vars:
   - ANTHROPIC_API_KEY
   - GMAIL_SENDER
   - GMAIL_APP_PASSWORD
   - GMAIL_RECIPIENT
5. Railway auto-deploys and runs `python main.py --schedule`
6. Check Logs tab to confirm it's running

Free tier: 500 hours/month — enough for a weekly script.

---

## Customising

Edit config.py to:
- Add new portfolio positions
- Update thesis descriptions
- Add signal words
- Add watchlist companies
- Add Google Alert RSS URLs

The more specific your thesis descriptions, the better Claude filters.

---

## Cost

- Anthropic API: ~$2-3/month (weekly runs)
- Railway: Free tier sufficient
- Stratechery (optional): $15/month

---

## Troubleshooting

**ModuleNotFoundError:** Make sure venv is active: `source venv/bin/activate`

**Gmail auth error:** Use App Password not your Gmail password. 2FA must be on.

**No articles fetched:** RSS feeds occasionally change URLs. Check trendforce.com/presscenter for current feed URL.

**Claude returns empty:** Check ANTHROPIC_API_KEY is correct at console.anthropic.com
