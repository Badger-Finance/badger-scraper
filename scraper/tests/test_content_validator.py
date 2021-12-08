import pytest

from scraper.constants import BADGER_APP_URL
from scraper.content_validator import validate_tags
from scraper.webdriver import fetch_data


@pytest.fixture
def discord_mock(mocker):
    mocker.patch("scraper.discord.Webhook.from_url")


def test_validator__happy(mocker, discord_mock, mock_webdriver):
    discord = mocker.patch("scraper.content_validator.send_ok_to_discord")
    validate_tags()
    assert discord.called


def test_validator__spoiled(mocker, discord_mock, mock_webdriver):
    discord = mocker.patch("scraper.content_validator.alert_to_discord")
    data = fetch_data(BADGER_APP_URL)
    data_compare = hash('<!DOCTYPE html><html itemscope '
                        'itemtype="https://schema.org/QAPage" class="html__responsive ">')
    validate_tags()
    assert discord.called
