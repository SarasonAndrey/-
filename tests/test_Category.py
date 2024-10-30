def test_Category_count(Category_1):
    assert Category_1.name == "оборудование"
    assert Category_1.description == "музыкальный"
    assert Category_1.products == ["магнитола", "плеер"]


def test_Category_count_1(Category_2):
    assert Category_2.name == "мебель"
    assert Category_2.description == "для спальни"
    assert Category_2.products == ["кровать", "диван"]
