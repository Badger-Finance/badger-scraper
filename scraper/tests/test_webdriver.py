import os

import pytest
from selenium.common.exceptions import WebDriverException

from scraper.constants import BADGER_APP_URL
from scraper.webdriver import webdriver_session


def test_webdriver__happy(mock_webdriver):
    with webdriver_session() as driver:
        driver.get(BADGER_APP_URL)
        content = driver.page_source
    assert content == '<!DOCTYPE html> <html><body><h1>My First Heading</h1><p>' \
                      'My first paragraph.</p></body></html>'


def test_webdriver__invalid_exec_path(mock_webdriver):
    # Case when driver is not properly installed
    os.environ['CHROMEDRIVER_PATH'] = "123"
    with pytest.raises(WebDriverException):
        with webdriver_session():
            pass
