from src.product import Product


class Category:
    name: str
    description: str
    products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, list_products):
        self.name = name
        self.description = description
        self.__products = list_products
        Category.category_count += 1
        Category.product_count += len(list_products) if list_products else 0

    def add_product(self, products):
        self.__products.append(products)

    @property
    def products(self):
        desc_products = []
        for products in self.__products:
            desc_products.append(f'{products.name}, {products.price} руб. Остаток: {products.quantity} шт.')
        return desc_products

    @products.setter
    def products(self, products: Product):
        self.__products.append(products)
        Category.product_count += 1
