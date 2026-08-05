from parsers.base import BaseParser

class DummyParser(BaseParser):
    def __init__(self):
        super().__init__("Dummy")

    def run(self):
        html = self.fetch("https://example.com")
        print(f"Получено {len(html)} символов")
