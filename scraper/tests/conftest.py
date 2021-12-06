import pytest


@pytest.fixture
def mock_webdriver(mocker):
    mocker.patch(
        "scraper.webdriver.webdriver.Chrome.get"
    )
    mocker.patch(
        "scraper.webdriver.webdriver.Chrome.page_source",
        '<!DOCTYPE html> '
        '<html>'
        '<body>'
        '<h1>My First Heading</h1>'
        '<p>My first paragraph.</p>'
        '</body>'
        '</html>'
    )
