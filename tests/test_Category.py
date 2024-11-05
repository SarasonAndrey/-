def test_Category_init(Category1):
    assert Category1.name == "оборудование"
    assert Category1.description == "музыкальный"
    assert Category1.products == ["магнитола", "плеер"]


def test_Category2(Category2):
    assert Category2.name == "мебель"
    assert Category2.description == "для спальни"
    assert Category2.products == ["кровать", "диван"]

    assert Category2.number_of_categories == 1
    assert Category2.number_of_products == 2


def test_Category3(Category3):
    assert Category3.name == ""
    assert Category3.description == ""
    assert Category3.products == [""]
