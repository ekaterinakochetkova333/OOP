import pytest


def test_init_smartphone(smartphone_init):
    """Тесты для проверки класса смартфонов"""
    assert smartphone_init.name == "Iphone 15"
    assert smartphone_init.description == "512GB, Gray space"
    assert smartphone_init.price == 210000.0
    assert smartphone_init.quantity == 8
    assert smartphone_init.efficiency == 98.2
    assert smartphone_init.model == "15"
    assert smartphone_init.memory == 512
    assert smartphone_init.color == "Gray space"


def test_smartphone_add(smartphone2, smartphone3):
    """Тесты проверяющие работу метода сложения"""
    assert smartphone2 + smartphone3 == 241000.0


def test_smartphone_add_error(smartphone2, grass1):
    with pytest.raises(TypeError):
        result = smartphone2 + grass1