from src.product import Product


class Smartphone(Product):
    """Класс Смартфон"""
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Метод сложения позволяющий складывать товары только из одинаковых классов продуктов"""
        if type(other) is Smartphone:
            return self.price + other.price
        raise TypeError
