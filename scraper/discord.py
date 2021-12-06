import os

from discord import RequestsWebhookAdapter
from discord import Webhook


def alert_to_discord():
    webhook = Webhook.from_url(
        os.getenv("DISCORD_WEBHOOK_URL"),
        adapter=RequestsWebhookAdapter(),
    )
    webhook.send('Badger site is spoiled', username='Badger Scraper Bot')
