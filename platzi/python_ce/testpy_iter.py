text = "cadena de texto"
iter_text = iter(text)

print('iter_text', iter_text)

for item_char in iter_text:
    print('item_char', item_char)

print("\n", "--------------------------------------------------")
print("Crear iterador para los número impares, usando range para crear los números")

limit = 10
odd_iter = iter(range(1, limit+1, 2))

for num in odd_iter:
    print("num: ", num)

print("\n", "--------------------------------------------------")
print("Generators -> función que crea una secuencia de números")

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

print("\n", "Generators -> fibonacci")

def fibonacci(limit):
    a, b = 0, 1

    while a <= 10:
        yield a
        a, b = b, a + b

str_result = ''

for num in fibonacci(10):
    if str_result != '':
        str_result = str_result + ', ' + str(num)
    else:
        str_result = str(num)
    
print(str_result)

#Ejercicio crear generadores para imprimir numeros pares e impares
print("\n", "--------------------------------------------------")
print("Generators -> función que crea una lista de números e imprime los pares y los impares")

def str_numbers_even_odd(limit):
    iter_numbers_evens = iter(range(0, limit+1, 2))
    iter_numbers_odds = iter(range(1, limit+1, 2))

    str_even = ''

    for i in iter_numbers_evens:
        if str_even != '':
            str_even = str_even + ', ' + str(i)
        else:
            str_even = str(i)

    str_odd = ''

    for i in iter_numbers_odds:
        if str_odd != '':
            str_odd = str_odd + ', ' + str(i)
        else:
            str_odd = str(i)

    print(str_even)
    print(str_odd)

def generator_number_even(limit):
    iter_numbers_evens = iter(range(0, limit+1, 2))

    for i in iter_numbers_evens:
        if i != 0:
            yield i

def generator_number_odd(limit):
    iter_numbers_odds = iter(range(1, limit+1, 2))

    for i in iter_numbers_odds:
        yield i

def print_numbers_even_odd(limit):
    for element in generator_number_even(limit):
        print(element)

    print('-----------------------------------------')

    for element in generator_number_odd(limit):
        print(element)

str_numbers_even_odd(10)
print('\n')
print_numbers_even_odd(10)


