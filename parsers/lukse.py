from bs4 import BeautifulSoup

from core.parser import BaseParser


class LukseParser(BaseParser):
    name = "LUKSE"

    def parse(self):
        url = "https://lukse.ru/"
        html = self.get(url)

        print(f"Получено {len(html)} символов")

        soup = BeautifulSoup(html, "lxml")

        print(soup.title.string if soup.title else "Без заголовка")
