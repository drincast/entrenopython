#Decorador que comprueba si un empleado tiene un rol en especifico
def check_access(required_role):
    try:
        def decorator(func):            
            def wrapper(employee):
                #Comprobar si el empleado tiene rol 'admin'
                print(required_role, employee['role'])
                if employee.get('role') == required_role:
                    return func(employee)
                else:
                    print(f"ACCIÓN DENEGADA. Solo los usuarios con rol {required_role} pueden realizar la acción")
                    return False
        
            return wrapper
        return decorator
    except Exception as ex:
        print(ex)


def log_action(call_delete_function):
    def decorator(func):
        def wrapper(employee):
            if(call_delete_function):
                print(f"Registrando evento para el empleado {employee['name']}")
                return func(employee)
            else:
                print(f"Registrando evento para el empleado {employee['name']}")

        return wrapper
    return decorator


@check_access('admin')
@log_action(True)
def delete_employee(employee):
    try:
        print(f"Empleado {employee['name']} eliminado \n")
    except Exception as ex:
        print(ex)

admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}

delete_employee(admin)
delete_employee(employee)