import os

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from contextlib import contextmanager


@contextmanager
def webdriver_session() -> WebDriver:
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--remote-debugging-port=9222')
    driver = webdriver.Chrome(
        executable_path=os.getenv('CHROMEDRIVER_PATH'),
        options=options
    )
    yield driver
    driver.quit()


def fetch_data(url: str) -> str:
    with webdriver_session() as driver:
        driver.get(url)
        return driver.page_source
