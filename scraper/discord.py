import os

from discord import RequestsWebhookAdapter
from discord import Webhook

from scraper.constants import BADGER_APP_URL
from scraper.constants import DISCORD_ALERT_ROLE


def alert_to_discord(count_difference: int, endpoint: str):
    webhook = Webhook.from_url(
        os.getenv("DISCORD_WEBHOOK_URL"),
        adapter=RequestsWebhookAdapter(),
    )
    webhook.send(
        f"<{BADGER_APP_URL}{endpoint}> might be malformed. "
        f"Has different amount of <script> tags than it's secured running copy. "
        f"Count tag difference: {count_difference}. "
        f"{DISCORD_ALERT_ROLE}",
        username='Badger Scraper Bot',
    )


def send_ok_to_discord(amount_of_tags: int, endpoint: str):
    webhook = Webhook.from_url(
        os.getenv("DISCORD_WEBHOOK_URL"),
        adapter=RequestsWebhookAdapter(),
    )
    webhook.send(
        f"<{BADGER_APP_URL}{endpoint}> website content is identical to it's secured running copy. "
        f"Amount of tags: {amount_of_tags}. "
        "Badgers can be chill :badger:",
        username='Badger Scraper Bot',
    )
