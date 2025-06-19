from src.product import Product


class Category:
    """Класс категорий"""
    name: str
    description: str
    products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, list_products):
        """Метод инициализации экземпляра класса. Значения атрибутов экземпляра."""
        self.name = name
        self.description = description
        self.__products = list_products
        Category.category_count += 1
        Category.product_count += len(list_products) if list_products else 0

    def __str__(self):
        result = str(sum(map(lambda x: x.quantity, self.__products)))
        return f"{self.name}, {"количество продуктов:"} {result}"


    def add_product(self, products):
        """Метод добавления товара в категорию"""
        self.__products.append(products)

    @property
    def products(self):
        """Геттер, выводить список товаров в виде строк в формате:
        Название продукта, 80 руб. Остаток: 15 шт."""
        desc_products = []
        for products in self.__products:
            desc_products.append(f"{str(products)}")
        return desc_products

    @products.setter
    def products(self, products: Product):
        self.__products.append(products)
        Category.product_count += 1


