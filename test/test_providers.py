import unittest
from unittest.mock import Mock

from shortener.database import UrlModel
from shortener.providers import UrlProviders


class TestUrlProviders(unittest.TestCase):
    def setUp(self):
        self.obj = UrlProviders()  # Replace with the name of your class
        self.obj.session = Mock()  # Create a mock object for self.session

    def test_get_url_providers_with_existing_url(self):
        existing_url = UrlModel(original_url="http://example.com")
        self.obj.session.query().filter_by().first.return_value = existing_url

        result = self.obj.get_url_providers("http://example.com")

        self.assertEqual(result, existing_url)

    def test_get_url_providers_with_non_existing_url(self):
        self.obj.session.query().filter_by().first.return_value = None

        result = self.obj.get_url_providers("http://example.com")

        self.assertIsNone(result)

    def test_add_url(self):
        new_url = UrlModel(original_url="http://example.com", shortcode="test12")
        self.obj.session.add.return_value = new_url

        result = self.obj.add_url(original_url="http://example.com", shortcode="test12")

        self.assertEqual(result.original_url, new_url.original_url)
        self.assertIsNot(result.shortcode, None)

    def test_get_url_by_shortcode_with_existing_url(self):
        url = UrlModel(original_url="http://example.com")
        self.obj.session.query().filter_by().first.return_value = url

        result = self.obj.get_url_by_shortcode("http://example.com")

        self.assertEqual(result, url)

    def test_get_url_by_shortcode_with_non_existing_url(self):
        self.obj.session.query().filter_by().first.return_value = None

        result = self.obj.get_url_by_shortcode("http://example.com")

        self.assertIsNone(result)
