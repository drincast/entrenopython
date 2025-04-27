#pythonico impresion de lista usando list compresion

numbers = [1,2,3,4,5]
squares = []

for number in numbers:
    square = number * number
    squares.append(square)

print(numbers, ' Cuadrados =>', squares)

squares = [x**2 for x in numbers]
print(f"\n{numbers}", ' Cuadrados =>', squares)


#PEP 8
# camel case nombre de clases
# funciones, variables snake case
# indentación 4 espacios
# longitud de línea sugerida 79 por línea
# espaciado de operador, un espacio antes y uno después
class Calculator:
    def add_numbers(self, first_number, second_number):
        result = first_number + second_number 
        return result

calc = Calculator()