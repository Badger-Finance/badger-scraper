from scraper.constants import SCRAPE_ENDPOINTS
from scraper.scraper import scrape


def test_scrape(mocker, mock_webdriver):
    discord = mocker.patch("scraper.content_validator.send_ok_to_discord")
    scrape()
    assert discord.call_count == len(SCRAPE_ENDPOINTS)
