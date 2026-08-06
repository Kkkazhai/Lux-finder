from dataclasses import dataclass


@dataclass
class Product:
    shop: str
    brand: str
    title: str
    article: str
    price: int
    old_price: int | None
    url: str
    image: str
