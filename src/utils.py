import json
import os

from src.Category import Category
from src.Product import Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def product_category_data_json(data):
    categorys = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categorys.append(Category(**category))
    return categorys


if __name__ == "__main__":
    products_list = read_json("../data/products.json")
    print(products_list)
    function = product_category_data_json(products_list)

    print(function[0].name)
    print(function[0].products)
