from bs4 import BeautifulSoup

from core.parser import BaseParser


class LukseParser(BaseParser):
    name = "LUKSE"

    def parse(self):
        url = "https://lukse.ru/catalog/"
        html = self.get(url)

        with open("lukse.html", "w", encoding="utf-8") as f:
            f.write(html)

        soup = BeautifulSoup(html, "lxml")

        print("HTML сохранен")
        print(soup.title.string if soup.title else "Нет title")
