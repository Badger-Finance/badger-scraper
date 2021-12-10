import pytest

from scraper.constants import BADGER_APP_COMPARE_URL
from scraper.constants import BADGER_APP_URL
from scraper.content_validator import calculate_amount_of_tags
from scraper.content_validator import validate_tags
from scraper.webdriver import fetch_data


@pytest.fixture
def discord_mock(mocker):
    mocker.patch("scraper.discord.Webhook.from_url")


def test_validator__happy(mocker, discord_mock, mock_webdriver):
    discord = mocker.patch("scraper.content_validator.send_ok_to_discord")
    data = fetch_data(BADGER_APP_URL)
    data_to_compare = fetch_data(BADGER_APP_COMPARE_URL)
    validate_tags(data, data_to_compare, "/endpoint")
    assert discord.called


def test_validator__spoiled(mocker, discord_mock, mock_webdriver):
    discord = mocker.patch("scraper.content_validator.alert_to_discord")
    data = fetch_data(BADGER_APP_URL)
    data_compare = ('<!DOCTYPE html><html itemscope '
                    'itemtype="https://schema.org/QAPage" class="html__responsive ">')
    validate_tags(data, data_compare, "/endpoint")
    assert discord.called


def test_calculate_amount_of_tags():
    assert calculate_amount_of_tags("<script>asdkjsaed</script>", "script") == 1
    assert calculate_amount_of_tags("<script>asdkjsaed</script>", "body") == 0
