def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError('El divisor no puede ser 0')
    return num1 / num2

if __name__ == "__main__":
    print('Operaciones')
    res_1 = addition(3,4)
    print(f'Suma: {res_1}')
    print(divide(10,7))

