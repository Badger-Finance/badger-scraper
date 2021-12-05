from scraper.constants import BADGER_APP_URL
from scraper.webdriver import get_webdriver


def test_fetch_html_content__happy():
    with get_webdriver() as driver:
        driver.get(BADGER_APP_URL)
        content = driver.page_source
    assert content is not None
