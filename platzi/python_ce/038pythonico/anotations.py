from typing import Optional, Union

class Employee:
    name: str
    age: int
    salary: float

    def __init__(self, name:str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def intro(self) -> str:
        try:
            return f"Hola, me llamo {self.name} tengo {self.age}"
        except Exception as ex:
            print(ex)

def add_employee_ids(id1: int, id2:int) -> int:
    return id1 + id2

def find_employee(employee_ids: list[int], employee_id: int) -> Optional[int]:
    """
    Busca un ID de empleado en una lista de IDs y devuelve el valor si existe.

    Parámetros:
    employee_ids (list[int]): Lista de IDs de empleados.
    employee_id (int): ID a buscar.

    Retorna:
    Optional[int]: El ID encontrado o None si no existe en la lista.
    """
    if employee_id in employee_ids:
        return employee_id
    return None

def process_salary(salary: Union[int, float]) -> float:
    """
    Procesa un salario que puede ser entero o flotante y lo devuelve como flotante.

    Parámetros:
    salary (Union[int, float]): Un salario que puede ser un entero o flotante.

    Retorna:
    float: El salario convertido a flotante.
    """
    return float(salary)

print(add_employee_ids(10, 65))

emp1 = Employee('Nana', 35, 4000.0)
print(emp1.intro())