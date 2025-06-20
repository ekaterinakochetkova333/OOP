def test_lawngrass_init(lawngrass_init):
    assert lawngrass_init.name == "Газонная трава"
    assert lawngrass_init.description == "Элитная трава для газона"
    assert lawngrass_init.price == 500.0
    assert lawngrass_init.quantity == 20
    assert lawngrass_init.country == "Россия"
    assert lawngrass_init.germination_period == "7 дней"
    assert lawngrass_init.color == "Зеленый"
