import json
import os

from src.Category import Category
from src.Product import Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


if __name__ == '__main__':
    data = read_json('../data/products.json')
    print(data)
