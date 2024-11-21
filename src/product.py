class Product:
    name: str  # Название
    description: str  # Описание
    price: float  # Цена
    quantity: int  # Колличество в наличии

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return


# if __name__ == "__main__":
#     product = Product("Патифон", "старый", 123.3, 3)
#
#     print(product.name)
#     print(product.description)
#     print(product.price)
#     print(product.quantity)
#     print(product.new_product)
