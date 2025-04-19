import math
import random


#generar un numero entero pseudo-aleatorio
random_number = random.randint(1,10)
print('numero aleatorio', random_number)

#Hallar el área y perimetro de un circulo
radius = random_number
area = math.pi * radius**2
perimeter = 2 * math.pi * radius
print(f"área y perimetro del circulo con radio = {radius}")
print('área', area)
print('perimetro', perimeter)

#elegir colores aleatorio
colors = ['Rojo', 'Azul', 'Verde', 'Amarillo', 'Morado', 'Naranja']
random_color = random.choice(colors)
print('color aleatorio', random_color)

#Barajar una lista de cartas
cards = ['As', 'Rey', 'Reina', 'Jota', '10']
random.shuffle(cards)
print(cards)



