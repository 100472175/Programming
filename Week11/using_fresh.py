from product import Product
from fresh_product import FreshProduct
from date import Date

p = Product('Chairs', 12.99)
fp = FreshProduct('apples', 1.2, Date(12, 'january', 2022))
print(p)
print(fp)
fp.sale()
print(fp)
