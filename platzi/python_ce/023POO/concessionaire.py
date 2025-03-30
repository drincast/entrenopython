from tabulate import tabulate

############## Class definitons 
class Vehicle:
    def __init__(self, available, brand, condition, color, name, price, type, ):
        self.available = available
        self.brand = brand
        self.color = color
        self.name = name
        self.price = price
        self.type = type
        self.condition = condition

    def sold(self):
        self.available = False

class User:
    def __init__(self, balance, name, user_id):
        self.balance = balance
        self.name = name
        self.user_id = user_id

        self.purchased_cars = []

    def buy_car(self, car, concessionaire):
        try:
            if car.available:
                if self.balance >= car.price:
                    self.balance -= car.price
                    concessionaire.balance += car.price
                    concessionaire.cars_sale.remove(car)
                    car.sold()                
                    self.purchased_cars.append(car)
                    print(f"{self.name} Compraste El vehículo {car.name} - {car.brand} por {car.price}")
                else:
                    raise ValueError("{self.name} no tienes fondos suficientes para comprarlo, estudia en PLATZI para ganar masssss :)")
            else:
                print(f"{self.name} el vehículo {car.name} - {car.brand} No esta disponible")
        except Exception as ex:
            print(ex)        

    def show_user_data(self):
        print(f"Nombre: {self.name}")
        print(f"Balance: {self.balance}")
        car_list = tool_get_car_list(self.purchased_cars)
        print(tabulate(car_list
                       , headers=["Disponible", "Marca", "Color", "Nombre", "Precio", "Tipo", "Condición"]
                       , tablefmt="pretty"))

    def sell_car(self, car, concessionaire):
        sale_price = (car.price - (car.price*0.1))
        self.balance = self.balance + sale_price
        car.price = sale_price
        concessionaire.buy_used_car(car)
        self.purchased_cars.remove(car)
        print(f"Has vendido el {car.name} - {car.brand} a {sale_price}, felicidades o ¿no?")

    def show_my_cars(self):
        print(f"Los carros de {self.name}")
        car_list = tool_get_car_list(self.purchased_cars)
        print(f"carriñios {self.purchased_cars}")

class Concessionaire:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.cars_sale = []

    def add_car(self, car):
        self.cars_sale.append(car)

    def sell_car(self, car):
        self.balance += car.price
        self.cars_sale.remove(car)

    def buy_used_car(self, car):
        profit_price = car.price + (car.price * 0.05)
        car.price = profit_price
        self.add_car(car)        

    def show_cars(self):
        print(f"Concesionario {self.name}")
        print(f"Carriñios a la venta")
        car_list = tool_get_car_list(self.cars_sale)
        print(tabulate(car_list
                       , headers=["Disponible", "Marca", "Color", "Nombre", "Precio", "Tipo", "Condición"]
                       , tablefmt="pretty"))

############## Funtions definitons 

def tool_get_car_list(object):
    try:
        car_list = [[c.available, c.brand, c.color, c.name, c.price, c.type, c.condition] for c in object]
        return car_list
    except Exception as ex:
        print(ex)
    

#############################################################

#los carriñios
vehicle1 = Vehicle(True, "Toyota", "Nuevo", "Rojo", "Corolla", 25000, "Sedán")
vehicle2 = Vehicle(True, "Honda", "Usado", "Azul", "Civic", 18000, "Hatchback")
vehicle3 = Vehicle(False, "Ford", "Nuevo", "Blanco", "Mustang", 35000, "Deportivo")
vehicle4 = Vehicle(True, "Chevrolet", "Usado", "Negro", "Camaro", 22000, "Deportivo")
vehicle5 = Vehicle(True, "Nissan", "Nuevo", "Gris", "Altima", 28000, "Sedán")
vehicle6 = Vehicle(False, "Volkswagen", "Usado", "Verde", "Jetta", 15000, "Sedán")
vehicle7 = Vehicle(True, "BMW", "Nuevo", "Plateado", "X5", 45000, "SUV")
vehicle8 = Vehicle(True, "Mercedes-Benz", "Usado", "Dorado", "C-Class", 30000, "Sedán")
vehicle9 = Vehicle(False, "Audi", "Nuevo", "Azul Marino", "A4", 40000, "Sedán")
vehicle10 = Vehicle(True, "Hyundai", "Usado", "Naranja", "Elantra", 17000, "Sedán")

#los peoples jeje
user1 = User(50000, "Alice", 1)
user2 = User(20000, "Bob", 2)
user3 = User(100000, "Charlie", 3)

#y los iluminatis, con esto se comprueba la tierra plana esferica
# Crear un objeto Concessionaire
concessionaire1 = Concessionaire(100000, "AutoIluminyMax")

concessionaire1.cars_sale.append(vehicle1)
concessionaire1.cars_sale.append(vehicle2)
concessionaire1.cars_sale.append(vehicle3)
concessionaire1.cars_sale.append(vehicle4)
concessionaire1.cars_sale.append(vehicle5)
concessionaire1.cars_sale.append(vehicle6)
concessionaire1.cars_sale.append(vehicle7)
concessionaire1.cars_sale.append(vehicle8)
concessionaire1.cars_sale.append(vehicle9)
concessionaire1.cars_sale.append(vehicle10)

print("___________________________________________________________________________________")
print(f"Balance: {concessionaire1.balance}")
concessionaire1.show_cars()

print("\n Compradores ...")
print(vars(user1))
print(vars(user2))
print(vars(user3))

#print(user1.get_dict_show_user_data(user1))

user1.buy_car(vehicle1, concessionaire1)
user2.buy_car(vehicle2, concessionaire1)
user3.buy_car(vehicle3, concessionaire1)

print("\n Compradores ...")
print("--------------------------------------------------------------------------------")
user1.show_user_data()
user2.show_user_data()
user3.show_user_data()

print("\n concesionario ...")
print(f"Balance: {concessionaire1.balance}")
concessionaire1.show_cars()

print("\n usuario vende ...")
user1.sell_car(vehicle1, concessionaire1)

print("\n Compradores ...")
print("--------------------------------------------------------------------------------")
user1.show_user_data()

print("\n concesionario ...")
print(f"Balance: {concessionaire1.balance}")
concessionaire1.show_cars()

print("___________________________________________________________________________________")