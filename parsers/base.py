import requests

class BaseParser:
    def __init__(self, name):
        self.name = name

    def fetch(self, url):
        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=30
        )
        response.raise_for_status()
        return response.text
