import random
import re
import string
from http import HTTPStatus

from typing import Any

from shortener.database import UrlModel
from .dataclasses import Response
from .providers import UrlProviders


class UrlServices:
    def __init__(self, providers: UrlProviders):
        self.providers = providers
        self.regex = re.compile(
            r"(?:\S+(?::\S*)?@)?"  # username:password@
            r"(?P<domain>[^\s\.:]+\.[^\s]{2,})"  # domain
        )

    def generate_shortcode(self) -> str:
        return "".join(random.choices(string.ascii_lowercase + string.digits, k=6))

    def create_response(
        self, status: int, message: str, data: Any = None, errors: str = None
    ) -> Response:
        return Response(status=status, message=message, data=data, errors=errors)

    def is_valid_url(self, url: str) -> bool:
        return True if re.match(self.regex, url) else False

    def get_shortcode(self, original_url: str) -> Response:
        if not self.is_valid_url(url=original_url):
            return self.create_response(
                HTTPStatus.BAD_REQUEST,
                HTTPStatus.BAD_REQUEST.phrase,
                errors="The text isn't a valid URL",
            )

        shortcode_response = self.get_url(original_url)
        if shortcode_response.status == HTTPStatus.OK:
            return shortcode_response
        new_shortcode = self.generate_shortcode()
        new_url = self.add_url(original_url, new_shortcode)
        data_response = {"shortcode": new_url.shortcode}
        return self.create_response(
            HTTPStatus.CREATED, HTTPStatus.CREATED.phrase, data_response
        )

    def get_url(self, url: str) -> Response:
        existing_url = self.providers.get_url_providers(original_url=url)
        if existing_url:
            data_response = {"shortcode": existing_url.shortcode}
            return self.create_response(
                HTTPStatus.OK, HTTPStatus.OK.phrase, data_response
            )
        return self.create_response(
            HTTPStatus.NOT_FOUND, HTTPStatus.NOT_FOUND.phrase, errors="Url Not found"
        )

    def add_url(self, url: str, shortcode: str) -> UrlModel:
        return self.providers.add_url(url, shortcode)

    def get_url_by_shortcode(self, shortcode):
        existing_url = self.providers.get_url_by_shortcode(shortcode=shortcode)
        if existing_url:
            data_response = {"original_url": existing_url.original_url}
            return self.create_response(
                HTTPStatus.OK, HTTPStatus.OK.phrase, data_response
            )
        return self.create_response(
            HTTPStatus.NOT_FOUND,
            HTTPStatus.NOT_FOUND.phrase,
            errors="Shortcode Not found",
        )
