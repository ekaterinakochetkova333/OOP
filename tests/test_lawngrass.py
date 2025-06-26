import pytest


def test_lawngrass_init(lawngrass_init):
    """Тесты для проверки класса газонной травы"""
    assert lawngrass_init.name == "Газонная трава"
    assert lawngrass_init.description == "Элитная трава для газона"
    assert lawngrass_init.price == 500.0
    assert lawngrass_init.quantity == 20
    assert lawngrass_init.country == "Россия"
    assert lawngrass_init.germination_period == "7 дней"
    assert lawngrass_init.color == "Зеленый"


def test_lawngrass_add(grass1, grass2):
    """Тесты проверяющие работу метода сложения"""
    assert grass1 + grass2 == 950.0


def test_lawngrass_add_error(grass1, smartphone2):
    with pytest.raises(TypeError):
        result = grass1 + smartphone2
