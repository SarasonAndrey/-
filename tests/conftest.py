import pytest

from src.Category import Category
from src.Product import Product


@pytest.fixture
def Product_1():
    return Product(name="Патифон", description="старый", prise="123.3", quantity="3")

@pytest.fixture
def Product_2():
    return Product(name="777", description="", prise="123.3", quantity="")

@pytest.fixture
def Product_3():
    return Product(name="", description="", prise="", quantity="")


@pytest.fixture
def Category_1():
    return Category(
        name="оборудование", description="музыкальный", products=["магнитола", "плеер"]
    )


@pytest.fixture
def Category_2():
    return Category(
        name="мебель", description="для спальни", products=["кровать", "диван"]
    )
@pytest.fixture
def Category_3():
    return Category(
        name="", description="", products=[""]
    )