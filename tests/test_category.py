def test_category_init(category_1):
    assert category_1.name == "оборудование"
    assert category_1.description == "музыкальный"
    assert category_1.products == ["магнитола", "плеер"]


def test_category2(category_2):
    assert category_2.name == "мебель"
    assert category_2.description == "для спальни"
    assert category_2.products == ["кровать", "диван"]

    assert category_2.number_of_categories == 1
    assert category_2.number_of_products == 2


def test_category3(category_3):
    assert category_3.name == ""
    assert category_3.description == ""
    assert category_3.products == [""]
