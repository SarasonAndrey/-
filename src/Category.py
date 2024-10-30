class Category:
    name: str  # Название
    description: str  # Описанме
    products: list  # Список товаров по категориям
    number_of_categories = 0  # Количество категорий
    number_of_products = 0  # Количество товаров

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.number_of_categories += 1
        Category.number_of_products += 1


if __name__ == "__main__":
    categoty = Category("оборудование", "музыкальный", ["магнитола", "плеер"])
    categoty = Category("мебель", "для спальни", ["кровать", "диван"])

    print(categoty.name)
    print(categoty.description)
    print(categoty.products)
    print(Category.number_of_categories)
    print(Category.number_of_products)
