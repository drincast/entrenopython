import random
#Clase Order
#validar el monto del pedido es mayor a un minimo (ejemplo 50)
#un método de clase que permita crear un pedido aplicando un descuento
# el descuento se aplica si el monto es mayor al minimo, de lo contrario no

class Order:
    AMOUNT_MIN = random.choice(range(40, 500, 50))
    GLOBAL_DISCOUNT = random.choice(range(10, 30, 5))

    def __init__(self):
        try:
            self._amount = 0
            self.discount = 0
        except Exception as ex:
            print(ex)

    @property
    def amount(self):
        try:
            return self._amount
        except Exception as ex:
            print(ex)

    @amount.setter
    def amount(self, new_amount: int):
        try:
            self._amount = new_amount
        except Exception as ex:
            print(ex)

    @amount.deleter
    def amount(self):
        try:
            del self._amount
        except Exception as ex:
            print(ex)

    @classmethod
    def create_order(cls, amount):
        discount = 0
        if cls.validate_amount(amount, cls.AMOUNT_MIN):
            discount = cls.calculate_tax(amount, cls.GLOBAL_DISCOUNT)

        total_order = amount - discount

        print(f"\nEl total de la orden es de {total_order}")
        print(f"Se aplico un descuento de {discount}")
        
    @classmethod
    def update_global_discount(cls, new_discount):
        try:
            cls.GLOBAL_DISCOUNT = new_discount
        except Exception as ex:
            print(ex)

    @staticmethod
    def calculate_tax(amount, tax_rate):
        try:
            discount = amount * (tax_rate / 100)
            print(f"Se aplicara un descuento del {tax_rate} %")
            print(f"Descuento para la venta {discount}")
            return discount
        except Exception as ex:
            print(ex)

    @staticmethod
    def validate_amount(amount, amount_min):
        '''
        Description: valida que el monto sea mayor al monto minimo
        Parameters:
            *args: los productos
        Returs: El total de la venta
        '''

        try:
            is_valid = True

            print(f"El monto minimo es {amount_min}")
            print(f"El monto del pedido es {amount}")

            if amount <= amount_min:
                print("no se aplica descuento")
                is_valid = False

            return is_valid
        except Exception as ex:
            print(ex)
    
    def show_info_to_apply_discount(self):
        try:
            print(f"Descuento a aplicar {self.GLOBAL_DISCOUNT} %")
            print(f"Se aplica si el monto es mayor a {self.AMOUNT_MIN}")
        except Exception as ex:
            print(ex)

#pedido 1
order1 = Order()
order1.amount = random.choice(range(50, 5000, 10))
order1.show_info_to_apply_discount()
# Order.validate_amount(order1.amount, order1.AMOUNT_MIN)
Order.create_order(order1.amount)
    
