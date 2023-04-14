import pytest
from unittest import mock
from shortener.database import UrlModel


def create_UrlModel_object() -> UrlModel:
    return UrlModel(original_url="www.test.com", shortcode="test12")


@pytest.fixture
def not_existing_url() -> str:
    return ["a", "b", ["c"]]
