from date import Date
from product import Product


class FreshProduct(Product):
    # The parenthesis is the inheritance indicator
    def __init__(self, name: str, price: str, expiration: Date):
        super().__init__(name, price)
        self.expiration = expiration

    def rotten_sale(self):
        self.price = 0

    def __str__(self):
        # return (self.name + ": " + str(self.price) + "€" + "expires on" + str(self.expiration))
        # With the supper, we use the same method we have inherited.
        return super().__str__() + " expires on" + str(self.expiration)

    def __eq__(self):
        return super().__eq__(other) and self.expiration == other.expiration
