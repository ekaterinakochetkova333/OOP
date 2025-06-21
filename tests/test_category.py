import pytest


def test_init_category(category_init):
    """Тесты для проверки класса категорий"""
    assert category_init.name == "Смартфоны"
    assert category_init.description == ("Смартфоны, как средство не только коммуникации, "
                                         "но и получения дополнительных функций для удобства жизни")
    assert len(category_init.products) == 3

    assert category_init.category_count == 1
    assert category_init.product_count == 3


def test_category_products_property(category_init):
    """Тест проверяющий геттер"""
    assert category_init.products == ['Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.',
                                      'Iphone 15, 210000.0 руб. Остаток: 8 шт.',
                                      'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.',]


def test_category_products_setter(category_init, product_init):
    """Тест проверяющий сеттер"""
    assert len(category_init.products) == 3
    category_init.products = product_init
    assert len(category_init.products) == 4


def test_category_str(category_init):
    assert str(category_init) == "Смартфоны, количество продуктов: 27"


def test_category_products_setter_error(category_init):
    with pytest.raises(TypeError):
        category_init.products = 1
