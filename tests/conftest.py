import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_1():
    return Product(name="Патифон", description="старый", price="123.3", quantity="3")


@pytest.fixture
def product_2():
    return Product(name="777", description="", price="123.3", quantity="")


@pytest.fixture
def product_3():
    return Product(name="", description="", price="", quantity="")


@pytest.fixture
def category_1():
    return Category(
        name="оборудование", description="музыкальный", products=["магнитола", "плеер"]
    )


@pytest.fixture
def category_2():
    category_2.number_of_categories = 0
    category_2.number_of_products = 0
    return Category(
        name="мебель", description="для спальни", products=["кровать", "диван"]
    )


@pytest.fixture
def category_3():
    return Category(name="", description="", products=[""])


@pytest.fixture
def product_data():
    return Product(name="Патифон", description="старый", price="123.3", quantity="3")


@pytest.fixture
def new_product(cls, product_data):
    return cls(name="Патифон", description="старый", price="123.3", quantity="3")


@pytest.fixture
def test_add_product(self, new_products: Product):
    return self.__products.append(new_products) == "Samsung Galaxy S23 Ultra"
    return Category.number_of_products == 1


@pytest.fixture
def products_list(self):
    return self == Product(
        name="Патифон", description="старый", price="123.3", quantity="3"
    )
