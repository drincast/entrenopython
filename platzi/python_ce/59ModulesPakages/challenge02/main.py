from ecommerce.inventory.stock import get_stock
from ecommerce.sales.orders import set_order

products = [['patinete', 10], ['Laptop', 20], ['Manillas', 50]]
orders = [['patinete', 1], ['Laptop', 2], ['Manillas', 10]]

for item in products:
    get_stock(item)

print()

for item in orders:
    set_order(item)