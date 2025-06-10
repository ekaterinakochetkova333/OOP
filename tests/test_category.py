def test_init_category(category_init):
    assert category_init.name == "Смартфоны"
    assert category_init.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(category_init.products) == 3

    assert category_init.category_count == 1
    assert category_init.product_count == 3
