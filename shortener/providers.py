from typing import Any

from .database import get_session_from_database, UrlModel


class UrlProviders:
    def __init__(self):
        session = get_session_from_database()
        self.session = session()

    def get_url_providers(self, original_url: str) -> UrlModel | None:
        existing_url = self.session.query(UrlModel).filter_by(original_url=original_url).first()
        if existing_url:
            return existing_url
        return None

    def add_url(self, original_url: str, shortcode: str) -> UrlModel:
        new_url = UrlModel(original_url=original_url, shortcode=shortcode)
        self.session.add(new_url)
        self.session.commit()
        self.session.refresh(new_url)
        return new_url

    def get_url_by_shortcode(self, shortcode: str) -> UrlModel | None:
        url = self.session.query(UrlModel).filter_by(shortcode=shortcode).first()
        if url:
            return url
        return None
