from src.product import Product


class LawnGrass(Product):
    """Класс трава газонная"""
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Метод сложения позволяющий складывать товары только из одинаковых классов продуктов"""
        if type(other) is LawnGrass:
            return self.price + other.price
        else:
            raise TypeError