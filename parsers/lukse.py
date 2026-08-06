from bs4 import BeautifulSoup
from core.parser import BaseParser


class LukseParser(BaseParser):
    name = "LUKSE"

    def parse(self):
        print("1. Старт")

        url = "https://lukse.ru/catalog/"
        print("2. Делаем запрос")

        html = self.get(url)

        print("3. Ответ получен")

        with open("lukse.html", "w", encoding="utf-8") as f:
            f.write(html)

        print("4. Файл сохранен")

        soup = BeautifulSoup(html, "lxml")

        print("5. HTML обработан")

        if soup.title:
            print(soup.title.string)
