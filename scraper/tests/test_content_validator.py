import pytest

from scraper.constants import BADGER_APP_URL
from scraper.constants import BADGER_APP_COMPARE_URL
from scraper.hash_content_validator import compare_hashes
from scraper.hash_content_validator import fetch_data


@pytest.fixture
def discord_mocker(mocker):
    return mocker.patch("scraper.discord.Webhook.from_url")


def test_validator__happy(discord_mocker, mock_webdriver):
    data = fetch_data(BADGER_APP_URL)
    data_compare = fetch_data(BADGER_APP_COMPARE_URL)
    compare_hashes(hash(data), hash(data_compare))
    assert not discord_mocker.called


def test_validator__spoiled(discord_mocker, mock_webdriver):
    data = fetch_data(BADGER_APP_URL)
    data_compare = hash('<!DOCTYPE html><html itemscope '
                        'itemtype="https://schema.org/QAPage" class="html__responsive ">')
    compare_hashes(hash(data), data_compare)
    assert discord_mocker.called
