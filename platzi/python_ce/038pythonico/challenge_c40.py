import random
import json

#variables
number_records = 7
# Listas de nombres masculinos y femeninos
male_names = ["Carlos", "Juan", "Luis", "Pedro", "Miguel", "Diego", "Fernando", "José", "Manuel", "Andrés"]
female_names = ["María", "Ana", "Isabel", "Sofía", "Paula", "Lucía", "Valeria", "Camila", "Lorena", "Gabriela"]
# list of all names
list_all_names = male_names + female_names

#list of ages
list_ages = random.choices(list(range(20, 90)), k=number_records)
list_salaries = random.choices(list(range(100, 3000, 100)), k=number_records)
selected_names = random.choices(list_all_names, k=number_records)

#for of records specified
list_dic_records = []

#for result
list_of_selected = []

#salary to compare
salary_to_compare = 0

#scramble the list of names
random.shuffle(list_all_names)

#generated of records specified
# for index in range(0, number_records):
#     dic = {'Name': selected_names[index], 'Age': list_ages[index], 'Salary':list_salaries[index]}
#     list_dic_records.append(dic)

list_dic_records = [
    {'Name': selected_names[index], 'Age': list_ages[index], 'Salary': list_salaries[index]}
    for index in range(number_records)
]

print("---- Lista de Personas ----")
for index in list_dic_records:
    print(index)
    # print(json.dumps(index, indent=10, ensure_ascii=False))
print()

def earn_more_than(list_persons:list, salary_more_than:float):
    '''
    Description:
        funcion que asigna a la variable global list_of_selected, los registros
        que tengan un salario mayor a salary_more_than
    Parameters:
        list_persons: lista de registros de personas con edad y salario.
        salary_more_than: valor para el salario a validar
    returns:
        Lista de los registross con salario  mayor a salary_more_than
    '''
    try:
        list_of_selected = [item for item in list_persons if item['Salary'] > salary_more_than ]
        return list_of_selected, salary_more_than
    except Exception as ex:
        print(ex)

list_of_selected, salary_to_compare = earn_more_than(list_dic_records, random.choice(list(range(100, 3000, 100))))
# earn_more_than(list_dic_records, random.choice(list(range(100, 3000, 100))))

print('-----------------------------------------------------------')
print(f"Salario a comparar -> {salary_to_compare}\n")
print("---- Personas que cumplen con la condición ----")
for index in list_of_selected:
    print(index)