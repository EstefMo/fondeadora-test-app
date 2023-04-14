from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch

from shortener.dataclasses import Response
from shortener.providers import UrlProviders
from shortener.services import UrlServices
from test.conftest import create_url_model_object


class TestUrlServices(TestCase):
    def setUp(self):
        self.providers = UrlProviders()
        self.services = UrlServices(self.providers)

    def test_generate_shortcode(self):
        result = self.services.generate_shortcode()
        print(result)
        assert isinstance(result, str)
        assert len(result) == 6

    def test_create_response_with_data(self):
        data_response = {"data": "test"}
        result = self.services.create_response(
            HTTPStatus.OK, HTTPStatus.OK.phrase, data_response
        )
        assert isinstance(result, Response)
        assert result.status is not None
        assert result.data is not None

    def test_create_response_with_errors(self):
        result = self.services.create_response(
            HTTPStatus.OK, HTTPStatus.OK.phrase, errors="Url Not found"
        )
        assert isinstance(result, Response)
        assert result.status is not None
        assert result.errors is not None

    @patch(
        "shortener.providers.UrlProviders.get_url_providers",
        return_value=create_url_model_object(),
    )
    def test_get_url_with_existing_url(self, get_url_response_mock):
        url = "www.test.com"
        result = self.services.get_url(url=url)
        get_url_response_mock.assert_called_with(original_url=url)
        assert result.status == HTTPStatus.OK
        assert result.data is not None
        assert len(result.data["shortcode"]) == 6

    @patch("shortener.providers.UrlProviders.get_url_providers", return_value=None)
    def test_get_url_with_non_existing_url(self, get_url_response_mock):
        url = "www.test.com"
        result = self.services.get_url(url=url)
        get_url_response_mock.assert_called_with(original_url=url)
        assert result.status == HTTPStatus.NOT_FOUND
        assert result.errors is not None

    @patch(
        "shortener.providers.UrlProviders.get_url_providers",
        return_value=create_url_model_object(),
    )
    def test_get_shortcode_with_existing_url(self, get_url_response_mock):
        url = "www.test.com"
        result = self.services.get_shortcode(original_url=url)
        get_url_response_mock.assert_called_with(original_url=url)
        assert result.status == HTTPStatus.OK
        assert result.data is not None
        assert len(result.data["shortcode"]) == 6

    @patch(
        "shortener.providers.UrlProviders.add_url",
        return_value=create_url_model_object(),
    )
    @patch("shortener.providers.UrlProviders.get_url_providers", return_value=None)
    def test_get_shortcode_adding_new_url(
        self, get_url_response_mock, add_url_response_mock
    ):
        url = "www.test.com"
        result = self.services.get_shortcode(original_url=url)
        add_url_response_mock.assert_called_once()
        get_url_response_mock.assert_called_with(original_url=url)
        assert result.status == HTTPStatus.CREATED
        assert result.data is not None
        assert len(result.data["shortcode"]) == 6

    @patch(
        "shortener.providers.UrlProviders.get_url_by_shortcode",
        return_value=create_url_model_object(),
    )
    def test_get_url_by_shortcode_with_existing_url(
        self, get_url_by_shortcode_response_mock
    ):
        shortcode = "test12"
        result = self.services.get_url_by_shortcode(shortcode=shortcode)
        get_url_by_shortcode_response_mock.assert_called_with(shortcode=shortcode)
        assert result.status == HTTPStatus.OK
        assert result.data is not None
        assert result.data["original_url"] is not None

    @patch("shortener.providers.UrlProviders.get_url_by_shortcode", return_value=None)
    def test_get_url_by_shortcode_with_non_existing_url(
        self, get_url_by_shortcode_response_mock
    ):
        shortcode = "test12"
        result = self.services.get_url_by_shortcode(shortcode=shortcode)
        get_url_by_shortcode_response_mock.assert_called_with(shortcode=shortcode)
        assert result.status == HTTPStatus.NOT_FOUND
        assert result.errors is not None
        assert result.errors == "Shortcode Not found"
