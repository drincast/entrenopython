#retorn True si un número es mayor a 0, si no retorna False
#retorna True si el balance es positivo
def is_positive(value):
    is_positive = True
    
    if value <= 0:
        is_positive = False

    return is_positive


#calcula el balance
def calculate_balance(income, expense):
    return income - expense

#retorna True si el balance es positivo
def is_balance_positive(income, expense):
    balance = calculate_balance(income, expense)
    response = is_positive(balance)

    return response
