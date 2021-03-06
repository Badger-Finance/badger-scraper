import os

BADGER_APP_URL = "https://app.badger.com"
BADGER_APP_COMPARE_URL = os.getenv("BADGER_APP_COMPARE_URL") or "https://badger-dapp.netlify.app"
DISCORD_ALERT_ROLE = "<@&917489227770523668>"
SCRAPE_ENDPOINTS = [
    "/",
    "/bridge",
    "/guarded",
    "/digg",
    "/ibBTC",
    "/boost",
    "/leaderboard",
]
