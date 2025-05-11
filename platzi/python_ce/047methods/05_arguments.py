class Employee:
    def __init__(self, name, *args, **kwargs):
        try:
            self.name = name
            self.skills = args
            self.detail = kwargs
        except Exception as ex:
            print(ex)

    def show_employee(self):
        try:
            print(f"Employee: {self.name}")
            print(f"Skills: {self.skills}")
            print(f"Detail: {self.detail}")
        except Exception as ex:
            print(ex)

employee = Employee('Max', 'Python', 'Java', 'C++', age=30, city='Bogotá')
employee.show_employee()
print(type(employee.skills))
