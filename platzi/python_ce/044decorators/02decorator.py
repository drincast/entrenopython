def check_access(func):
    try:
        def wrapper(employee):
            #Comprobar su el empleado tiene rol 'admin'
            if employee.get('role') == 'admin':
                return func(employee)
            else:
                print("ACCIÓN DENEGADA. Solo los administradores pueden acceder")
        
        return wrapper
    except Exception as ex:
        print(ex)

@check_access
def delete_employee(employee):
    try:
        print(f"Empleado {employee['name']} eliminado")
    except Exception as ex:
        print(ex)

admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}

delete_employee(admin)
delete_employee(employee)