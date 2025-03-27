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

    def buy_car(self, car):
        if car.available:
            if self.balance >= car.price:
                car.sold()
                self.purchased_cars.append(car)
                print(f"Compraste El vehículo {car.name} - {car.brand} por {car.sold}")
            else:
                raise ValueError("No tienes fondos suficientes para comprarlo, estudia en PLATZI para ganar masssss :)")
        else:
            print(f"El vehículo {car.name} - {car.brand} No esta disponible")

    def sell_car(self, car, concessionaire):
        sale_price = (car.price - (car.price*0.1))
        self.balance = self.balance + sale_price
        car.price = sale_price
        concessionaire.buy_used_car(car)            
        print(f"Has vendido el {car.name} - {car.brand} a {sale_price}, felicidades o ¿no?")

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


