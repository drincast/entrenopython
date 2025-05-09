employees = list()

def add_employee(name: str, area: str, code: int):
    try:
        global employees

        employee = {'Nombre': name, 'Area': area, 'Codigo': code}
        employees.append(employee)
    except Exception as ex:
        print(ex)

def remove_employee(code: int):
    try:
        global employees

        new_employees = [ item for item in employees if item['Codigo'] == code]

        if len(new_employees) > 0:
            employees.remove(new_employees[0])
    except Exception as ex:
        print(ex)



employees.append({'Nombre': 'Alvaro', 'Area': 'Materiles', 'Codigo': 1})

print(employees)

if __name__ == '__main__':
    add_employee('Maria', 'Laboratorio', 30)
    add_employee('Oscar', 'Drivers', 5)
    add_employee('Milena', 'Ropa', 10)
    add_employee('Alvaro', 'Materiales', 1)
    add_employee('Karime', 'Zonal', 3)

    print('---- Lista de empleados ----')
    print(employees)

    print('\n---- Eliminamos un empleado ----')
    remove_employee(30)
    print(employees)

