import pytest

from shortener.database import UrlModel


def create_url_model_object() -> UrlModel:
    return UrlModel(original_url="www.test.com", shortcode="test12")
