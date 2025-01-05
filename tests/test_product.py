import pytest

from src.product import Product


def test_product_init(product_1):
    assert product_1.name == "Патифон"
    assert product_1.description == "старый"
    assert product_1.price == "123.3"
    assert product_1.quantity == "3"


def test_product2(product_2):
    assert product_2.name == "777"
    assert product_2.description == ""
    assert product_2.price == "123.3"
    assert product_2.quantity == ""


def test_product3(product_3):
    assert product_3.name == ""
    assert product_3.description == ""
    assert product_3.price == ""
    assert product_3.quantity == ""


def test_new_product(new_product):
    assert new_product.name == "Гусли"
    assert new_product.description == "старый"
    assert new_product.price == "777777"

    assert new_product.quantity == 1


def test_product__str__(product__str__):
    assert product__str__ == ("Барабан", "200 руб." "Остаток: 2 шт.")


def test_product_price__add__(products_list, new_product):
    assert 123.3 * 3 + 777777 * 1 == 778146.9


def test_add_product_zero():
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product(
            "Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0
        )
