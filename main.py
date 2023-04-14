from fastapi import FastAPI
from shortener.services import UrlServices
from shortener.providers import UrlProviders 
from shortener.dataclasses import Response


app = FastAPI()
url_providers = UrlProviders()
url_services = UrlServices(url_providers)


@app.post('/{url:path}')
def shorten_url(url: str) -> Response:
    return  url_services.get_shortcode(url)
   

@app.get('/{shortcode}')
def get_original_url(shortcode: str) -> Response:
    return url_services.get_url_by_shortcode(shortcode)