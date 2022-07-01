class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if type(price) != float and type(price) != int:
            raise TypeError("The price must be a number")
        elif price >= 0:
            self.__price = price
        else:
            raise ValueError("Price is less than 0, really?")

    def __str__(self):
        return self.name + ": " + str(self.price) + "€"

    def sale(self):
        self.price = self.price / 2
