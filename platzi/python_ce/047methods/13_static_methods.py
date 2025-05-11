class Order:
    global_discount = 10

    def __init__(self, amount):
        try:
            self.amount = amount
        except Exception as ex:
            print(ex)

    @classmethod
    def update_global_discount(cls, new_discount):
        try:
            cls.global_discount = new_discount
        except Exception as ex:
            print(ex)

    @staticmethod
    def calculate_tax(amount, tax_rate):
        try:
            return amount * (tax_rate / 100)
        except Exception as ex:
            print(ex)

Order.update_global_discount(15)
print(Order.global_discount)
print()
print(Order.calculate_tax(1000, 18))