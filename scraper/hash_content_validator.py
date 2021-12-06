from scraper.discord import alert_to_discord
from scraper.webdriver import webdriver_session


def fetch_data(url: str) -> str:
    with webdriver_session() as driver:
        driver.get(url)
        return driver.page_source


def compare_hashes(content: int, compare_content: int) -> None:
    if content != compare_content:
        alert_to_discord()
