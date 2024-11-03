import json
import os
from typing import List

from src.Category import Category
from src.Product import Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def product_category_data_json(data):
    categorys = []
    for category in data:
        products = []
        for product in data("products"):
            products.append(product(**Product))
        data("products") = products
        categorys.append(category(**Category))
    return categorys


if __name__ == '__main__':
    products = read_json('../data/products.json')
    function = product_category_data_json(products)
    print(function)
