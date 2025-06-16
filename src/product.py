class Product:
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

    @classmethod
    def new_product(cls, product):
        """Класс-метод, принимать на вход параметры товара в словаре и возвращает созданный объект класса Product."""
        name = product["name"]
        description = product["description"]
        price = product["price"]
        quantity = product["quantity"]
        return Product(name, description, price, quantity)

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
