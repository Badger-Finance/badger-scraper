import logging

from scraper.discord import alert_to_discord
from scraper.discord import send_ok_to_discord
from scraper.webdriver import webdriver_session


logger = logging.getLogger(__name__)


def fetch_data(url: str) -> str:
    with webdriver_session() as driver:
        driver.get(url)
        return driver.page_source


def compare_hashes(content: int, compare_content: int) -> None:
    if content != compare_content:
        alert_to_discord()
        logger.warning("Websites are different")
    else:
        send_ok_to_discord()
        logger.info("Websites are identical")
