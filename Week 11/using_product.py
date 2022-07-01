from product import Product
from fresh_product import FreshProduct
p = Product("Toys", 22.1)
print(p)
p.sale()
print(p)

fp = FreshProduct("Oranges", 1.1)
print(fp)
fp.sale()
print(fp)
fp.rotten_sale()
print(fp)