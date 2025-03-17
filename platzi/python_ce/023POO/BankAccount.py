
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        try:
            if self.is_active:
                if(amount > 0):
                    self.balance += amount
                    print(f"Se ha depositado {amount}. Saldo actual: {self.balance}")
                else:
                    raise ValueError("El monto debe ser mayor a 0")
            else:
                print("No se puede depositar, cuenta inactiva")
        except ValueError as ex:
            print(ex)
    
    def withdraw(self, amount):
        try:
            if self.is_active:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Se ha retirado {amount}. Saldo actual: {self.balance}")
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
            print(f'Saldo:', self.balance)
            print(f'Cuenta:', 'activa' if self.is_active else 'inactiva')
            print('----------------------------------------------------------')
        except Exception as ex:
            print(ex)

    def activate_account(self):
        try:
            self.is_active = True
            print("La cuenta ha sido activada")
        except Exception as ex:
            print(ex)
    
    def deactivate_account(self):
        try:
            self.is_active = False
            print("La cuenta ha sido desactivada")
        except Exception as ex:
            print(ex)
    

# Crear objetos de la clase BankAccount
account1 = BankAccount("Ana", 500)
account2 = BankAccount("Luis", 1000)

account1.deposit(0)
account1.deactivate_account()
account1.withdraw(100)
account1.activate_account()
account1.withdraw(1000)
account1.information_account()

account1.deposit(500)
account2.withdraw(100)
account1.deactivate_account()
account1.deposit(200)
account1.activate_account()
account1.deposit(200)

account1.information_account()
account2.information_account()

