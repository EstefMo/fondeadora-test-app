from pydantic import BaseModel


class UrlCreateRequest(BaseModel):
    original_url: str


class UrlRetrieveRequest(BaseModel):
    shortcode: str
