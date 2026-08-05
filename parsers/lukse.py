from bs4 import BeautifulSoup

from core.parser import BaseParser


class LukseParser(BaseParser):
    name = "LUKSE"

    def parse(self):
        url = "https://lukse.ru/"
        html = self.get(url)

        soup = BeautifulSoup(html, "lxml")

        print(f"Страница {self.name} загружена")

        return soup
