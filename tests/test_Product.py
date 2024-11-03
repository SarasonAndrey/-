def test_Product(Product_1):
    assert Product_1.name == "Патифон"
    assert Product_1.description == "старый"
    assert Product_1.prise == "123.3"
    assert Product_1.quantity == "3"


def test_Product2(Product_2):
    assert Product_2.name == "777"
    assert Product_2.description == ""
    assert Product_2.prise == "123.3"
    assert Product_2.quantity == ""


def test_Product3(Product_3):
    assert Product_3.name == ""
    assert Product_3.description == ""
    assert Product_3.prise == ""
    assert Product_3.quantity == ""
