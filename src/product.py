class Product:
    name: str  # Название
    description: str  # Описание
    price: float  # Цена
    quantity: int  # Колличество в наличии

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


# if __name__ == "__main__":
#     product = Product("Патифон", "старый", 123.3, 3)
#
#     print(product.name)
#     print(product.description)
#     print(product.price)
#     print(product.quantity)
