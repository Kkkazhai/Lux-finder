from abc import ABC, abstractmethod

import requests

from config import HEADERS, REQUEST_TIMEOUT


class BaseParser(ABC):
    name = "Unknown"

    def get(self, url: str) -> str:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.text

    @abstractmethod
    def parse(self):
        pass
