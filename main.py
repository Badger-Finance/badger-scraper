from scraper.constants import BADGER_APP_COMPARE_URL
from scraper.constants import BADGER_APP_URL
from scraper.hash_content_validator import compare_hashes
from scraper.helpers import subsctract_statis_js_files
from scraper.webdriver import fetch_data


def main() -> None:
    data = subsctract_statis_js_files(fetch_data(BADGER_APP_URL))
    data_compare = subsctract_statis_js_files(fetch_data(BADGER_APP_COMPARE_URL))
    compare_hashes(hash(data), hash(data_compare))


if __name__ == '__main__':
    main()
