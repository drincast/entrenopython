class Employee:
    def __init__(self, name, salary):
        try:
            self.name = name
            self._salary = salary
        except Exception as ex:
            print(ex)

    @property
    def salary(self):
        try:
            return self._salary        
        except Exception as ex:
            print(ex)

    @salary.setter
    def salary(self, new_salary):
        try:
            if new_salary < 0:
                raise ValueError("El salario no puede ser negativo")
            
            self._salary = new_salary
        except Exception as ex:
            print(ex)

    @salary.deleter
    def salary(self):
        try:
            print(f"El salario de {self.name} se ha eliminado")
            del self._salary
        except Exception as ex:
            print(ex)

    def show_employee(self):
        try:
            print(f"Empleado: {self.name}")
            print(f"Salario: {self._salary}")
        except Exception as ex:
            print(ex)

employee = Employee("Rossi", 3000)
print(employee.salary)
print("---------------------------------------\n")

employee.salary = 6000
print(employee.salary)

employee.salary = -6000
print(employee.salary)

del employee.salary
print(employee.salary)
employee.salary = 1000