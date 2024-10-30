class Product:
    name: str  # Название
    discription: str  # Описание
    prise: float  # Цена
    quantity: int  # Колличество в наличии

    def __init__(self, name, discription, prise, quantity):
        self.name = name
        self.discription = discription
        self.prise = prise
        self.quantity = quantity


if __name__ == "__main__":
    product = Product("Патифон", "старый", 123.3, 3)

    print(product.name)
    print(product.discription)
    print(product.prise)
    print(product.quantity)
