# ============================================================
# YOUR INVESTMENT THESIS MAP
# Edit this file to update your portfolio, watchlist,
# signal words, and newsletter settings.
# ============================================================

PORTFOLIO = {
    # ETFs — tracked via thesis drivers, not individual holdings
    "QQQ": {
        "type": "etf",
        "thesis": "Broad Nasdaq tech exposure — benefits from AI platform growth, big tech earnings",
        "thesis_drivers": ["big tech earnings", "AI capex", "cloud revenue", "Nasdaq", "Microsoft Azure", "Google Cloud", "AWS"],
    },
    "ICLN": {
        "type": "etf",
        "thesis": "Global clean energy — benefits from data center power demand, nuclear renaissance, energy transition",
        "thesis_drivers": ["clean energy", "nuclear power", "data center energy", "renewable energy policy", "power grid", "Bloom Energy", "First Solar"],
    },
    "SMH": {
        "type": "etf",
        "thesis": "Semiconductor ETF — Nvidia, TSMC, AMD, Broadcom. Benefits from AI chip demand supercycle",
        "thesis_drivers": ["semiconductor supply", "HBM memory", "chip demand", "Nvidia", "TSMC", "AMD", "Broadcom", "fab capacity", "AI chips", "NAND"],
    },
    "FLKR": {
        "type": "etf",
        "thesis": "South Korea — Samsung + SK Hynix HBM memory chips for AI. Exit review at year 7-8.",
        "thesis_drivers": ["SK Hynix", "Samsung memory", "HBM demand", "Korean semiconductor", "DRAM pricing", "memory supercycle", "South Korea AI"],
    },
    "GRID": {
        "type": "etf",
        "thesis": "Grid infrastructure — Vertiv, Quanta, Schneider, Eaton, ABB. Data center power and cooling.",
        "thesis_drivers": ["grid infrastructure", "Vertiv", "Quanta Services", "power infrastructure", "liquid cooling", "data center cooling", "ABB", "Eaton", "Schneider"],
    },
    # Individual stocks
    "CEG": {
        "type": "stock",
        "name": "Constellation Energy",
        "thesis": "Largest US nuclear operator. Long-term data center power contracts. Currently down from high — hold.",
        "thesis_drivers": ["nuclear power contracts", "data center energy", "Calpine acquisition", "Crane nuclear restart", "Constellation Energy"],
    },
    "TSLA": {
        "type": "stock",
        "name": "Tesla",
        "thesis": "EV + energy storage + autonomous driving. Long held since 2020.",
        "thesis_drivers": ["Tesla earnings", "EV demand", "Megapack", "autonomous driving", "energy storage", "robotaxi"],
    },
    "MSFT": {
        "type": "stock",
        "name": "Microsoft",
        "thesis": "Azure AI cloud + OpenAI partnership. Core compounder.",
        "thesis_drivers": ["Azure revenue", "Microsoft earnings", "OpenAI", "enterprise AI", "cloud growth", "Copilot"],
    },
    "GOOG": {
        "type": "stock",
        "name": "Alphabet / Google",
        "thesis": "AI + search dominance + Google Cloud. Antitrust headwind watch.",
        "thesis_drivers": ["Google earnings", "Gemini AI", "Google Cloud", "search revenue", "antitrust", "YouTube"],
    },
    "AMZN": {
        "type": "stock",
        "name": "Amazon",
        "thesis": "AWS cloud dominance + Anthropic investment + retail recovery.",
        "thesis_drivers": ["AWS revenue", "Amazon earnings", "Anthropic", "cloud infrastructure", "AWS AI"],
    },
    "AAPL": {
        "type": "stock",
        "name": "Apple",
        "thesis": "Services growth + Apple Intelligence + installed base monetisation.",
        "thesis_drivers": ["Apple earnings", "iPhone demand", "Apple Intelligence", "services revenue", "Vision Pro"],
    },
}

# ============================================================
# WATCHLIST — researching, not yet bought
# ============================================================
WATCHLIST = {
    "NOW": {
        "thesis": "ServiceNow — enterprise AI workflow layer. Anthropic partnership. August buy candidate at ₹60k.",
        "thesis_drivers": ["ServiceNow earnings", "agentic AI", "enterprise workflow", "Now Assist", "AI agents", "Anthropic ServiceNow"],
        "target_month": "August 2026",
    },
    "PLTR": {
        "thesis": "Palantir — AI data platform, government + enterprise. August buy candidate at ₹40k.",
        "thesis_drivers": ["Palantir earnings", "AIP platform", "government contracts", "enterprise AI", "US commercial revenue"],
        "target_month": "August 2026",
    },
    "SNDK": {
        "thesis": "SanDisk — pure-play NAND flash, AI storage layer. KV cache demand. Datacenter revenue +645% YoY. Entry timing unclear.",
        "thesis_drivers": ["SanDisk NAND", "KV cache", "AI storage", "NAND pricing", "datacenter storage"],
        "target_month": "Research ongoing",
    },
    "META": {
        "thesis": "Meta — AI-powered advertising flywheel. 700M Meta AI users, zero direct AI revenue yet. Monitoring for monetisation signal. Stage 4 candidate for September slot.",
        "thesis_drivers": ["Meta AI monetization", "Meta earnings", "Meta Compute", "Llama revenue", "Meta advertising AI", "Reality Labs"],
        "target_month": "Research Jul-Aug, decide September",
    },
    "SPCX": {
        "thesis": "SpaceX — rockets, Starlink, xAI, space data centers. IPO June 12 2026 at $135. Currently ~$153. Waiting for post-lock-up price discovery before buying.",
        "thesis_drivers": ["SpaceX earnings", "Starlink subscribers", "SPCX stock", "space data center", "xAI revenue", "Starship launch"],
        "target_month": "Watch — buy after 180-day lock-up expiry",
    },
    "MOD": {
        "thesis": "Modine — pure-play thermal management post-spinoff. 50-70% annual growth guided.",
        "thesis_drivers": ["Modine data center", "thermal management", "chiller demand", "liquid cooling spinoff"],
        "target_month": "Research ongoing",
    },
}

# ============================================================
# SIGNAL WORDS — Claude flags these as high priority
# The words that historically appear before a big move
# ============================================================
BULLISH_SIGNALS = [
    "sold out through",
    "customers prepaying",
    "supply cannot meet demand",
    "long-term supply agreement",
    "multi-year agreement",
    "backlog surged",
    "backlog growing",
    "record orders",
    "capacity fully committed",
    "inventory depleted",
    "demand exceeds supply",
    "pricing power",
    "strategic asset",
    "acquires",
    "acquisition",
    "partnership",
    "sold out",
    "prepayment",
]

BEARISH_SIGNALS = [
    "oversupply",
    "inventory correction",
    "customers delaying",
    "backlog cancellation",
    "capex cut",
    "capex reduction",
    "spending slows",
    "pricing pressure",
    "margin compression",
    "demand weakness",
    "guidance cut",
    "missed expectations",
    "inventory buildup",
]

# ============================================================
# UNEXPECTED CONNECTIONS — the ServiceNow moment detector
# Claude looks for cross-portfolio signals proactively
# ============================================================
UNEXPECTED_CONNECTION_TRIGGERS = [
    "partnership",
    "integration",
    "acquisition",
    "invest",
    "contract",
    "deal",
    "supply agreement",
]

# ============================================================
# RSS FEEDS
# ============================================================
RSS_FEEDS = [
    {
        "name": "TrendForce",
        "url": "https://www.trendforce.com/presscenter/rss",
        "type": "leading_indicator",
        "description": "Semiconductor supply/demand data — earliest signal source",
    },
    {
        "name": "Bloomberg Technology",
        "url": "https://feeds.bloomberg.com/technology/news.rss",
        "type": "confirmation",
        "description": "Tech news",
    },
    {
        "name": "Ars Technica",
        "url": "https://feeds.arstechnica.com/arstechnica/technology-lab",
        "type": "analysis",
        "description": "Tech analysis",
    },
    {
        "name": "Seeking Alpha Semiconductors",
        "url": "https://seekingalpha.com/feed/sector/technology/semiconductors.xml",
        "type": "analysis",
        "description": "Semiconductor analyst commentary",
    },
]

# Add your Google Alert RSS URLs here after setup at google.com/alerts
# Suggested alerts: "data center acquisition", "HBM memory demand",
# "semiconductor supply sold out", "nuclear power data center contract",
# "AI infrastructure capex", "Jensen Huang"
GOOGLE_ALERT_FEEDS = [
    "https://www.google.co.in/alerts/feeds/01425330569128522464/19844091331779924",
    "https://www.google.co.in/alerts/feeds/01425330569128522464/3021223753586575329",
    "https://www.google.co.in/alerts/feeds/01425330569128522464/3021223753586574303",
    "https://www.google.co.in/alerts/feeds/01425330569128522464/15560152635813350081",
    "https://www.google.co.in/alerts/feeds/01425330569128522464/15560152635813350644",
    "https://www.google.co.in/alerts/feeds/01425330569128522464/16364453294335925447",
    "https://www.google.co.in/alerts/feeds/01425330569128522464/16364453294335922357",
    "https://www.google.com/alerts/feeds/01425330569128522464/14338312367489043007",
    "https://www.google.co.in/alerts/feeds/01425330569128522464/19844091331779924",
    "https://www.google.co.in/alerts/feeds/01425330569128522464/3021223753586575329",
    "https://www.google.co.in/alerts/feeds/01425330569128522464/3021223753586574303",
    "https://www.google.co.in/alerts/feeds/01425330569128522464/15560152635813350081",
    "https://www.google.co.in/alerts/feeds/01425330569128522464/15560152635813350644",
    "https://www.google.co.in/alerts/feeds/01425330569128522464/16364453294335925447",
    "https://www.google.co.in/alerts/feeds/01425330569128522464/16364453294335922357",
    "https://www.google.co.in/alerts/feeds/01425330569128522464/19844091331779924",
    "https://www.google.co.in/alerts/feeds/01425330569128522464/3021223753586575329",
    "https://www.google.co.in/alerts/feeds/01425330569128522464/3021223753586574303",
    "https://www.google.co.in/alerts/feeds/01425330569128522464/15560152635813350081",
    "https://www.google.co.in/alerts/feeds/01425330569128522464/15560152635813350644",
]

# ============================================================
# EARNINGS WATCHLIST
# ============================================================
EARNINGS_WATCHLIST = [
    "Nvidia", "Micron", "SK Hynix", "Samsung",
    "Microsoft", "Google", "Amazon", "Apple", "Tesla",
    "Constellation Energy", "Vertiv", "GE Vernova",
    "Palantir", "ServiceNow", "Broadcom", "TSMC",
    "SanDisk", "Modine",
]

# ============================================================
# NEWSLETTER CONFIG
# ============================================================
NEWSLETTER = {
    "subject": "📊 Before It's Obvious — Weekly Briefing {date}",
    "send_day": "sunday",
    "send_hour": 8,          # 8am IST
    "lookback_days": 7,
    "max_items_per_source": 10,
    "stratechery_reminder": True,
}
