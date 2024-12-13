class Product:
    name: str  # Название
    description: str  # Описание
    price: float  # Цена
    quantity: int  # Колличество в наличии

    def __init__(
            self, name: object, description: object, price: object, quantity: object
    ) -> object:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product_data):
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: int):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __add__(self, other):
        if type(other) is Product:
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

