from collections import Counter, defaultdict

def count_products(orders: list[str]) -> defaultdict:
    product_count = defaultdict(int)
    for product in orders:
        product_count[product] += 1
    return product_count

orders = ['laptop', 'smartphone', 'laptop', 'tablet']
response = count_products(orders)
print(response)  # Output: defaultdict(<class 'int'>, {'laptop': 2, 'smartphone': 1, 'tablet': 1})


def count_sales(products: list[str]) -> Counter:
    return Counter(products)

products = ['laptop', 'smartphone', 'smartphone', 'laptop', 'tablet']
response = count_sales(products)
print(response)  # Output: Counter({'laptop': 2, 'smartphone': 2, 'tablet': 1})