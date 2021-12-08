from scraper.constants import BADGER_APP_COMPARE_URL
from scraper.constants import BADGER_APP_URL
from scraper.content_validator import validate_tags
from scraper.webdriver import fetch_data


def main() -> None:
    data = fetch_data(BADGER_APP_URL)
    data_to_compare = fetch_data(BADGER_APP_COMPARE_URL)
    validate_tags(data, data_to_compare)


if __name__ == '__main__':
    main()
