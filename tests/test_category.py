from src.category import Category
from src.product import Product


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


def test_category_property(category_1):
    assert category_1.name == "оборудование"
    assert category_1.description == "музыкальный"
    assert category_1.products == ["магнитола", "плеер"]


def test_add_product(self, new_products: Product):
    assert self.__products.append(new_products) == "Samsung Galaxy S23 Ultra"
    assert Category.number_of_products == 1


def test_products_list(self):
    assert self == Product(
        name="Патифон", description="старый", price="123.3", quantity="3"
    )

def test___str__(self):
    assert self == Product(name="Патифон", description="старый", price="123.3", quantity="3")
