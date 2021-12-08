import logging
from bs4 import BeautifulSoup

from scraper.constants import BADGER_APP_COMPARE_URL
from scraper.constants import BADGER_APP_URL
from scraper.discord import alert_to_discord
from scraper.discord import send_ok_to_discord
from scraper.webdriver import fetch_data

logger = logging.getLogger(__name__)


def calculate_amount_of_tags(content: str, tag: str) -> int:
    soup = BeautifulSoup(content)
    return len(soup.find_all(tag))


def validate_tags():
    data = fetch_data(BADGER_APP_URL)
    data_compare = fetch_data(BADGER_APP_COMPARE_URL)
    badger_site_tags_count = calculate_amount_of_tags(data, "script")
    target_site_tags_count = calculate_amount_of_tags(data_compare, "script")
    if badger_site_tags_count != target_site_tags_count:
        if badger_site_tags_count > target_site_tags_count:
            difference = badger_site_tags_count - target_site_tags_count
        else:
            difference = target_site_tags_count - badger_site_tags_count
        alert_to_discord(difference)
        logger.warning("Websites are different!")
    else:
        send_ok_to_discord(badger_site_tags_count)
        logger.info("Websites are identical")
