from scraper.constants import BADGER_APP_COMPARE_URL
from scraper.constants import BADGER_APP_URL
from scraper.constants import SCRAPE_ENDPOINTS
from scraper.content_validator import validate_tags
from scraper.json_logger import logger
from scraper.webdriver import fetch_data


def scrape():
    logger.info(
        "Validating Badger Endpoints",
        extra={'endpoints': SCRAPE_ENDPOINTS},
    )
    for endpoint in SCRAPE_ENDPOINTS:
        data = fetch_data(url=f"{BADGER_APP_URL}{endpoint}")
        data_to_compare = fetch_data(url=f"{BADGER_APP_COMPARE_URL}{endpoint}")
        validate_tags(data, data_to_compare, endpoint)
