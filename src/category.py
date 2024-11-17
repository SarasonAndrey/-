from src.product import Product


class Category:
    name: str  # Название
    description: str  # Описание
    products: list  # Список товаров по категориям

    number_of_categories = 0  # Количество категорий
    number_of_products = 0  # Количество товаров

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.number_of_categories += 1
        Category.number_of_products += len(self.__products)

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, products_new: Product):
        if isinstance(products_new, Product):
            self.__products.append(products_new)
            Category.count_products += 1
        else:
            raise TypeError



if __name__ == "__main__":
    category = Category("оборудование", "музыкальный", ["магнитола", "плеер"])
    category = Category("мебель", "для спальни", ["кровать", "диван"])
    category = Category("столы", "для кухни", ["складной стол", "стол тумба"])


    print(category.name)
    print(category.description)
    print(category.products)
    print(Category.number_of_categories)
    print(Category.number_of_products)
