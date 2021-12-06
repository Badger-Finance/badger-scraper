import os

from discord import RequestsWebhookAdapter
from discord import Webhook

from scraper.constants import BADGER_APP_COMPARE_URL
from scraper.constants import BADGER_APP_URL
from scraper.constants import DISCORD_ALERT_ROLE

WEBHOOK = Webhook.from_url(
    os.getenv("DISCORD_WEBHOOK_URL"),
    adapter=RequestsWebhookAdapter(),
)


def alert_to_discord():
    WEBHOOK.send(
        f"<{BADGER_APP_URL}> website content is not equal to <{BADGER_APP_COMPARE_URL}> content!!!"
        f"{DISCORD_ALERT_ROLE}",
        username='Badger Scraper Bot',
    )


def send_ok_to_discord():
    WEBHOOK.send(
        f"<{BADGER_APP_URL}> website content is identical to <{BADGER_APP_COMPARE_URL}> content. "
        f"Badgers can be chill :badger:",
        username='Badger Scraper Bot',
    )
