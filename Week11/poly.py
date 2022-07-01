from product import Product
from fresh_product import FreshProduct
from date import Date
p = Product('Chairs', 12.99)
fp = FreshProduct('apples', 1.2, Date(12, 'january', 2022))
print(type(p))  # class 'product.Product'
print(type(fp))  # class 'fresh_product.FreshProduct
print(isinstance(p, Product))  # True
print(isinstance(fp, FreshProduct))  # True
print(isinstance(fp, Product))  # True, a human in an animal, a mammal is an animal, a human is a mammal.


