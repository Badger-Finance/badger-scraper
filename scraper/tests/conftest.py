import pytest


@pytest.fixture
def mock_webdriver(mocker):
    mocker.patch(
        "scraper.webdriver.webdriver.Chrome.get"
    )
    mocker.patch(
        "scraper.webdriver.webdriver.Chrome.page_source",
        "123",
    )
