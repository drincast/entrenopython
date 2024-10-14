print('\n', ' ---------------- listas ---------------- ')
vlist = []
print(vlist)
vlist = [1,2,3,4,5,6,7,8,9,0]
print(vlist)
del vlist
#print(vlist) del elimina de memoria la variable vlist

#slice
vlist = [1,2,3,4,5,6,7,8,9,0]
vlist_copy = vlist          #realiza una referencia a la memoria de la lista original
vlist_cp_slice = vlist[:]   #copia el contenido de la lista original en una nueva lista

del vlist[6]
print('vlist         ', vlist)
print('vlist_copy    ', vlist_copy)
print('vlist_cp_slice', vlist_cp_slice)

#lista de listas
print('\n', ' ---------------- listas de listas ---------------- ')
vlist = [[1,2,3],[4,5,6],[7,8,9]]
print(type(vlist))
print(vlist, vlist[2][2])

#tuplas
print('\n', ' ---------------- tuplas ---------------- ')
vtuple = (1,2,3,4,5,6,7,8,9,0)
print(type(vtuple))
print(vtuple, vtuple[5])
#vtuple[0] = 10  #tuple' object does not support item assignment

#diccionarios
print('\n', ' ---------------- diccionario ---------------- ')
vdictionary = {1:"uno", 2:"uno", 3:"tres"}
print(type(vdictionary))
print(vdictionary)

vinformation = {'nombre':'Carla', 'apellido':'Florida', 'altura':1.60, 'edad':29, 'pais':'Mexico'}
print('\n', vinformation)
del vinformation['pais']
print(vinformation)
print('keys', vinformation.keys())
print(type(vinformation.keys()))
print('values', vinformation.values())

pairs = vinformation.items()
print('\n', pairs)

#actualiza vinformation para que ahora tenga don conjunto de datos
vinformation = {'Carla':{'nombre':'Carla', 'apellido':'Florida', 'altura':1.60, 'edad':29, 'pais':'Mexico'}, 
                'Juan':{'nombre':'Juan', 'apellido':'Perez', 'altura':1.75, 'edad':34, 'pais':'Colombia'}}

print('\n', vinformation)
print(vinformation['Juan'])

#comprehensuion List
print('\n', ' ---------------- Comprehension List ---------------- ')
vsquares = [x**2 for x in range(1,11)]
print("Cuadrados:",vsquares)

vcelsius = [c+10 for c in range(-10, 30, 3)]
vfahrenheit = [(9/5)*c + 32 for c in vcelsius]

print(f"Celsius {vcelsius}")
print("temperatura en F: ", vfahrenheit)

#numeros pares
vevens = [x for x in range(1, 21) if x % 2 == 0]
print("\n", "numeros pares: ", vevens)

#matrices
print('\n', ' ---------------- Comprehension List Matrices ---------------- ')
vmatrix_base = [[1,2,3],
                [4,5,6],
                [7,8,9]]
# vmatrix_base = [[i for i in range(1,4)] for j in range(3)]
vmatrix_transposed = [[row[i] for row in vmatrix_base] for i in range(len(vmatrix_base[0]))]

#este seria la forma de imprimir la matriz con bucles, con comprehension list al parecer el ultimo ciclo es el primero que se ejecuta??
# t = []
# for i in range(len(vmatrix_base[0])):
#     t_row = []
#     for row in vmatrix_base:
#         t_row.append(row[i])
#     t.append(t_row)
# print(t)

print('vmatrix', vmatrix_base)
print('vmatrix', vmatrix_transposed)

#ejercicios de comprehension list
#Doble de los numeros -> crear una lista nueva con el doble de los nuemeros de la lista base
print('\n', ' ---------------- Ejercicios Comprehension List---------------- ')
print('Doble de los numeros')
vlist_base = [1,2,3,4,5]
vlist_double = [x*2 for x in vlist_base]
print('vlist_base: ', vlist_base)
print('vlist_double: ', vlist_double)

#Filtrar y Transformar en un Solo Paso -> lista ["sol", "mar", "montaña", "rio", "estrella"] obtener una nueva lista con las palabras 
#que tengan más de 3 letras y estén en mayúsculas.
print('\nFiltrar y Transformar en un Solo Paso')
vlist_base = ["sol", "mar", "montaña", "rio", "estrella", "Casa", "CASA"]
vlist_filter = [x for x in vlist_base if len(x) > 3 and x.isupper()]
print('vlist_base: ', vlist_base)
print('vlist_filter: ', vlist_filter)

#Crear un Diccionario con List Comprehension -> Tienes dos listas, una de claves ["nombre", "edad", "ocupación"] 
#y otra de valores ["Juan", 30, "Ingeniero"]. Crea un diccionario combinando ambas listas usando una List Comprehension.
vlist_keys = ["nombre", "edad", "ocupación"]
vlist_values = ["Juan", 30, "Ingeniero"]
#vdict_comp = {k: v for k, v in zip(vlist_keys, vlist_values)}
vdict_comp = {vlist_keys[i]: vlist_values[i] for i in range(len(vlist_keys))}
print('vlist_keys', vlist_keys)
print('vlist_values', vlist_values)
print('vdict_comp: ', vdict_comp)



