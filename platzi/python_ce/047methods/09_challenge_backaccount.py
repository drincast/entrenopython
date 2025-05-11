from datetime import datetime

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance
        self._is_active = True
        self.__transactions = []
    
    def _deposit(self, amount):
        try:
            if self._is_active:
                if(amount > 0):
                    self.__balance += amount
                    print(f"Se ha depositado {amount}. Saldo actual: {self.__balance}")
                    self.__transaction_record('deposito', amount)
                else:
                    raise ValueError("El monto debe ser mayor a 0")
            else:
                print("No se puede depositar, cuenta inactiva")
        except ValueError as ex:
            print(ex)
    
    def _withdraw(self, amount):
        try:
            if self._is_active:
                if amount <= self.__balance:
                    self.__balance -= amount
                    print(f"Se ha retirado {amount}. Saldo actual: {self.__balance}")
                    self.__transaction_record('retiro', amount)
                else:
                    #print("Fondos insuficientes")
                    raise ValueError(f"No pude retirar {amount}, fondos insuficientes")
            else:
                #print("No se puede retirar, cuenta inactiva")
                raise Exception("No se puede retirar, cuenta inactiva")
        except Exception as ex:
            print(ex)

    def information_account(self):
        try:
            print('\n----------------------------------------------------------')
            print(f'Dueño:', self.account_holder)
            print(f'Saldo:', self.__balance)
            print(f'Cuenta:', 'activa' if self._is_active else 'inactiva')
            print('----------------------------------------------------------')
        except Exception as ex:
            print(ex)

    def _activate_account(self):
        try:
            self._is_active = True
            print("La cuenta ha sido activada")
        except Exception as ex:
            print(ex)
    
    def _deactivate_account(self):
        try:
            self._is_active = False
            print("La cuenta ha sido desactivada")
        except Exception as ex:
            print(ex)

    def show_simple_transaction(self, transaction_type):
        try:
            print(f"Se realizo una transaccion de {transaction_type} a la cuenta {self.account_holder}")
        except Exception as ex:
            print(ex)

    def get_transactions(self):
        for transaction in self.__transactions:
            print(transaction)

    def __transaction_record(self, transaction_type, amount):
        try:
            transaction = f"[{datetime.now().strftime("%Y-%m-%d %H:%M")}] - Se realizó un {transaction_type} de {amount}"
            self.__transactions.append(transaction)
            self.show_simple_transaction(transaction_type)
        except Exception as ex:
            print(ex)
    

# Crear objetos de la clase BankAccount
account1 = BankAccount("Ana", 500)
account2 = BankAccount("Luis", 1000)

account1._deposit(0)
account1._deactivate_account()
account1._withdraw(100)
account1._activate_account()
account1._withdraw(1000)
account1.information_account()

account1._deposit(500)
account2._withdraw(100)
account1._deactivate_account()
account1._deposit(200)
account1._activate_account()
account1._deposit(200)

account1.information_account()
account1.get_transactions()

account2.information_account()
account2.get_transactions()

