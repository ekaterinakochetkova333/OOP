from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс товаров"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод инициализации экземпляра класса. Значения атрибутов экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()


    def __str__(self):
        """Метод возвращает строку в формате: Название продукта, X руб. Остаток: X шт. """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод возвращает сумму произведений цены у двух объектов."""
        return self.price + other.price

    @classmethod
    def new_product(cls, **product):
        """Класс-метод, принимать на вход параметры товара в словаре и возвращает созданный объект класса Product."""
        return cls(**product)

    @property
    def price(self):
        """Геттер возващает цену продукта"""
        return self.__price

    @price.setter
    def price(self, price):
        """Сеттер, проверяет цену товара на условие: цена равна или ниже нуля"""
        if float(price) <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        else:
            self.__price = price
            return
