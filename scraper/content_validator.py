from bs4 import BeautifulSoup

from scraper.discord import alert_to_discord
from scraper.discord import send_ok_to_discord
from scraper.json_logger import logger


def calculate_amount_of_tags(content: str, tag: str) -> int:
    soup = BeautifulSoup(content)
    return len(soup.find_all(tag))


def validate_tags(badger_html: str, target_html: str, endpoint: str):
    badger_site_tags_count = calculate_amount_of_tags(badger_html, "script")
    target_site_tags_count = calculate_amount_of_tags(target_html, "script")
    if badger_site_tags_count != target_site_tags_count:
        if badger_site_tags_count > target_site_tags_count:
            difference = badger_site_tags_count - target_site_tags_count
        else:
            difference = target_site_tags_count - badger_site_tags_count
        alert_to_discord(difference, endpoint)
        logger.warning("Websites are different!")
    else:
        send_ok_to_discord(badger_site_tags_count, endpoint)
        logger.info("Websites are identical")
