# Se realiza este ejecicio de concecionario de vehiculos teniendo encuenta que todo va a girar entorno al concecionario.
# osea todas las clases las maneja el concecionario siendo esta la clase que lidera la funcionalidad
# Aqui es una forma de astraer esta funcionalidad de la vida real, la otra seria ver dos clases por aparte que seria
# el concecionario y los compradores, esto sera un ejerccicio para resolver mas adelante ya que aqui se necesitaria
# referencia a objetos, inyeccion de dependencias

from tabulate import tabulate

############## Global Constans 
HEADERS_VEHICLE = ["Disponible", "Marca", "Color", "id", "Nombre", "Precio", "Tipo", "Condición"]
HEADERS_CUSTOMER = ["Habilitado", "balance", "Nombre", "Id"]

############## Class definitons 
class Vehicle:
    def __init__(self, available, brand, color, condition, id, name, price, type, ):
        self.available = available #puede ser que el vehiculo este en reparaciones
        self.brand = brand
        self.color = color
        self.condition = condition
        self.id = id
        self.name = name
        self.price = price
        self.type = type

    def sold(self):
        self.available = False

    def start_engine(self):
        raise NotImplementedError("Error: Método aun no implementado")
    
    def stop_engine(self):
        raise NotImplementedError("Error: Método aun no implementado")

    def tabular_print_info_vehicle(self):
        attribute_list = tool_transform_object_attributes_to_list_of_list(self)
        print(tabulate(attribute_list
                       , HEADERS_VEHICLE
                       , tablefmt="pretty"))

        # return {k: ("***" if k == "password" else v) for k, v in self.__dict__.items()}

class Bike(Vehicle):
    def __init__(self, available, brand, color, condition, id, name, price, type):
        super().__init__(available, brand, condition, color, id, name, price, type)

    def start_engine(self):
        if self.available:
            return(f"La bicicleta {self.name} esta en marcha")
        else:
            return(f"La bicicleta {self.name} no esta disponible")
    
    def stop_engine(self):
        if self.available:
            return(f"La bicicleta {self.name} se ha detenido")
        else:
            return(f"La bicicleta {self.name} no esta disponible")

class Car(Vehicle):
    def __init__(self, available, brand, color, condition, id, name, price, type):
        super().__init__(available, brand, color, condition, id, name, price, type)

    def start_engine(self):
        if self.available:
            return(f"El motor del carro {self.name} esta en marcha")
        else:
            return(f"El carro {self.name} no esta disponible")
    
    def stop_engine(self):
        if self.available:
            return(f"El motor del carro {self.name} se ha detenido")
        else:
            return(f"El carro {self.name} no esta disponible")

class Truck(Vehicle):
    def __init__(self, available, brand, color, condition, id, name, price, type):
        super().__init__(available, brand, color, condition, id, name, price, type)

    def start_engine(self):
        if self.available:
            return(f"El motor del camión {self.name} esta en marcha")
        else:
            return(f"El camión {self.name} no esta disponible")
    
    def stop_engine(self):
        if self.available:
            return(f"El motor del camión {self.name} se ha detenido")
        else:
            return(f"El camión {self.name} no esta disponible")
        

class Customer:
    def __init__(self, balance, name, user_id):
        self.available = True
        self.balance = balance
        self.name = name
        self.user_id = user_id

        self.purchased_vehicles = set()

    def add_vehicle(self, vehicle):
        try:
            self.purchased_vehicles.add(vehicle)
        except Exception as ex:
            print(ex)

    def buy_vehicle(self, vehicle, concessionaire):
        try:
            #se valida que el balance sea mayor al precio
            #Si se tiene balance indicamos que que quiere comprar
            #llama a dealership para realizar la compra            
            if self.balance >= vehicle.price:
                #llamar dealership para validar compra
                response = concessionaire.validate_vehicle_sale(self, vehicle)

                if response["response"] == False:
                    print('No se puede realizar la venta -> ', response["message"])
                    return
                
                concessionaire.sell_vehicle(self, vehicle)
                self.balance -= vehicle.price
                self.add_vehicle(vehicle)

                print(f"{self.name} Compraste El vehículo {vehicle.name} - {vehicle.brand} por {vehicle.price}")
            else:
                raise ValueError("{self.name} no tienes fondos suficientes para comprarlo, estudia en PLATZI para ganar masssss :)")
        except Exception as ex:
            print(ex)
            
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.user_id

    def show_user_data(self):
        print(f"Nombre: {self.name}")
        print(f"Balance: {self.balance}")
        vehicle_list = tool_get_vehicle_list(self.purchased_vehicles)
        
        if len(vehicle_list) > 0:
            print(tabulate(vehicle_list
                        , HEADERS_VEHICLE
                        , tablefmt="pretty"))
            print("\n")
        else:
            print("No tiene vehiculos \n")

    def sell_vehicle(self, vehicle, concessionaire):
        sale_price = (vehicle.price - (vehicle.price*0.1))
        vehicle.price = sale_price
        concessionaire.buy_used_car(vehicle)
        self.balance = self.balance + sale_price
        self.purchased_vehicles.remove(vehicle)
        print(f"{self.name} has vendido el {vehicle.name} - {vehicle.brand} a {sale_price}, felicidades o ¿no?")

    def show_my_vehicles(self):
        print(f"Los carros de {self.name}")
        vehicles_list = tool_get_vehicle_list(self.purchased_vehicles)
        print(f"carriñios {self.purchased_vehicles}")

    def tabular_print_info_customer(self):
        attribute_list = tool_transform_object_attributes_to_list_of_list(self)
        print(tabulate(attribute_list
                       , HEADERS_CUSTOMER
                       , tablefmt="pretty"))

class Concessionaire:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.vehicles_sale = set()
        self.customers = set()

    def add_vehicle(self, car):
        self.vehicles_sale.add(car)

    def add_customer(self, customer):
        self.customers.add(customer)

    def buy_used_car(self, car):
        profit_price = car.price + (car.price * 0.05)
        car.price = profit_price
        self.add_vehicle(car)        

    def get_vehicle_for_id(self, id):
        try:
            vehicle = next((v for v in self.vehicles_sale if v.id == id), None)
            return vehicle
        except Exception as ex:
            print(ex)

    def print_customer(self, customer):
        try:
            for element in self.customers:
                if customer == element:
                    element.tabular_print_info_customer()
        except Exception as ex:
            print(ex)

    def remove_customer(self, customer):
        self.customers.remove(customer)

    def sell_vehicle(self, custumer, vehicle):
        self.balance += vehicle.price
        self.vehicles_sale.remove(vehicle)

    def show_vehicles(self):
        print(f"Concesionario {self.name}")
        print(f"Carriñios a la venta")
        vehicle_list = tool_get_vehicle_list(self.vehicles_sale)
        print(tabulate(vehicle_list
                       , HEADERS_VEHICLE
                       , tablefmt="pretty"))
        
    def show_customers(self):
        print(f"Concesionario {self.name}")
        print(f"Lista de clientes")
        customers_list = tool_transform_object_attributes_to_list_of_list(self.customers)
        print(tabulate(customers_list
                       , HEADERS_CUSTOMER
                       , tablefmt="pretty"))

    def validate_customer(self, customer):
        response = dict()

        try:
            if len(self.customers) <= 0:
                response = {"response": False, "message": f"No tenemos clientes registrados en este momento"}
                return response
            
            exist = customer in self.customers
            #index_customer = {index for index, obj in enumerate(self.customers) if obj == customer}            
            response = {"response": exist, "message": "" if exist else f"El cliente {customer.get_name()} no esta en nuetra lista de clientes, por favor agregue el cliente a nuestra lista"}
            
            return response
        except Exception as ex:
            print(ex)

    def validate_vehicle_sale(self, customer, vehicle):
        response = dict()
        try:
            if not vehicle.available:
                response = {"response": False, "message": f"El vehiculo {vehicle.name} no esta disponible"}
                return response

            response = self.validate_customer(customer)

            if not response["response"]:
                return response

            #no se si se deba validar que customer tenga saldo ???
        
            return response
        except Exception as ex:
            print(ex)

############## Funtions definitons 

def tool_get_vehicle_list(object):
    try:
        vehicle_list = [[c.available, c.brand, c.color, c.id, c.name, c.price, c.type, c.condition] for c in object]
        return vehicle_list
    except Exception as ex:
        print(ex)

def tool_transform_object_attributes_to_list_cp(object):
    try:
        var_list = []
        list_of_list = []

        for key, val in object.__dict__.items():
            var_list.append(val)

        list_of_list.append(var_list)

        return list_of_list
    except Exception as ex:
        print(ex)

def tool_transform_object_attributes_to_list(object):
    var_list = []

    for key, val in object.__dict__.items():
        # if key != 'purchased_vehicles':
        if not isinstance(val, set):
            var_list.append(val)

    return var_list

def tool_transform_object_attributes_to_list_of_list(object):
    try:
        list_of_list = []

        if isinstance(object, set):
            for elemet in object:
                #var_list = []
                # for key, value in elemet.__dict__.items():
                #     # if key != 'purchased_vehicles':
                #     if not isinstance(value, set):
                #         var_list.append(value)

                list_of_list.append(tool_transform_object_attributes_to_list(elemet))
        else:
            # for key, val in object.__dict__.items():
            #     if key != 'purchased_vehicles':
            #         var_list.append(val)
            # list_of_list.append(var_list)

            list_of_list.append(tool_transform_object_attributes_to_list(object))

        return list_of_list
    except Exception as ex:
        print(ex)
    

#############################################################

#los carriñios
car1 = Car(True, "Toyota", "Nuevo", "Rojo", 1, "Corolla", 25000, "Sedán")
car2 = Car(True, "Honda", "Usado", "Azul", 2, "Civic", 18000, "Hatchback")
car3 = Car(False, "Ford", "Nuevo", "Blanco", 3, "Mustang", 35000, "Deportivo")
car4 = Car(True, "Chevrolet", "Usado", "Negro", 4, "Camaro", 22000, "Deportivo")
car5 = Car(True, "Nissan", "Nuevo", "Gris", 5, "Altima", 28000, "Sedán")
car6 = Car(False, "Volkswagen", "Usado", "Verde", 6, "Jetta", 15000, "Sedán")
car7 = Car(True, "BMW", "Nuevo", "Plateado", 7, "X5", 45000, "SUV")
car8 = Car(True, "Mercedes-Benz", "Usado", "Dorado", 8, "C-Class", 30000, "Sedán")
car9 = Car(False, "Audi", "Nuevo", "Azul Marino", 9, "A4", 40000, "Sedán")
car10 = Car(True, "Hyundai", "Usado", "Naranja", 10, "Elantra", 17000, "Sedán")
car11 = Car(True, "Volkswagen", "Nuevo", "Blanco", 11, "Golf", 20000, "hatchback")
car12 = Car(True, "BMW", "Usado", "Azul", 12, "Serie 3", 30000, "Sedán")

# bikes:
bike1 = Bike(True, "Giant", "Nuevo", "Negro", 13, "Trance X", 2500, "Cicla de montaña")
bike2 = Bike(False, "Scott", "Usado", "Gris", 14, "Scale 965", 1200, "Cicla de montaña")

#trucks
truck1 = Truck(True, "Volvo", "Nuevo", "Gris", 15, "FH16", 120000, "50 toneladas")
truck2 = Truck(False, "Mercedes-Benz", "Usado", "Blanco", 16, "Actros", 85000, "40 toneladas")

# print(vehicle10.__dict__.items())
# print(vars(vehicle10))
# print(vehicle10.tabular_print_info_vehicle())
# print(tool_transform_object_attributes_to_list(vehicle10))

# exit()

#los peoples jeje
customer1 = Customer(50000, "Alice", 1)
customer2 = Customer(20000, "Bob", 2)
customer3 = Customer(100000, "Charlie", 3)
customer4 = Customer(1000000, "Maria", 4)

#y los iluminatis, con esto se comprueba la tierra planaesferica
# Crear un objeto Concessionaire
concessionaire1 = Concessionaire(100000, "AutoIluminyMax")

#add vehicles
concessionaire1.add_vehicle(car1)
concessionaire1.add_vehicle(car2)
concessionaire1.add_vehicle(car3)
concessionaire1.add_vehicle(car4)
concessionaire1.add_vehicle(car5)
concessionaire1.add_vehicle(car6)
concessionaire1.add_vehicle(car7)
concessionaire1.add_vehicle(car8)
concessionaire1.add_vehicle(car9)
concessionaire1.add_vehicle(car10)
concessionaire1.add_vehicle(car11)
concessionaire1.add_vehicle(car12)
concessionaire1.add_vehicle(bike1)
concessionaire1.add_vehicle(bike2)
concessionaire1.add_vehicle(truck1)
concessionaire1.add_vehicle(truck2)

#add customers
concessionaire1.add_customer(customer1)
concessionaire1.add_customer(customer2)
concessionaire1.add_customer(customer3)

print("___________________________________________________________________________________")
print(f"Balance: {concessionaire1.balance}")
concessionaire1.show_vehicles()

print("\n Compradores ...")
# imp_customer = next((p for p in concessionaire1.customers if p.user_id == 2), None)
# imp_customer.tabular_print_info_customer()

# al ser un tipo set (conjuntos) no se puede acceder al dat por medio del indice
for element in concessionaire1.customers:
    element.tabular_print_info_customer()

# concessionaire1.customers[1].tabular_print_info_customer()
# concessionaire1.customers[2].tabular_print_info_customer()
# concessionaire1.customers[3].tabular_print_info_customer()

#print(user1.get_dict_show_user_data(user1))

print("\n Compradores Comprando Carriñios...")
print("--------------------------------------------------------------------------------")

# al ser un tipo set (conjuntos) no se puede acceder al dat por medio del indice
for element in concessionaire1.customers:
    if element.user_id == 1:
        element.buy_vehicle(concessionaire1.get_vehicle_for_id(1), concessionaire1)
    elif element.user_id == 2:
        element.buy_vehicle(concessionaire1.get_vehicle_for_id(2), concessionaire1)
    else:
        element.buy_vehicle(concessionaire1.get_vehicle_for_id(3), concessionaire1)

print("\n Compradores ...")
print("--------------------------------------------------------------------------------")
for element in concessionaire1.customers:
    element.show_user_data()

print("\n --------------------------------------------------------------------------------")
concessionaire1.show_customers()
# a = list()
# b = set()

# print(type(a), type(b))

# print(len(concessionaire1.customers), type(concessionaire1.customers))
# tool_transform_object_attributes_to_list_cp(concessionaire1.customers)

print("\n concesionario ...")
print(f"Balance: {concessionaire1.balance}")
concessionaire1.show_vehicles()

print("\n usuario vende ...")
imp_customer = next((p for p in concessionaire1.customers if p.user_id == 1), None)
imp_customer_vehicle = next((p for p in imp_customer.purchased_vehicles if p.id == 1), None)
imp_customer.sell_vehicle(car1, concessionaire1)

print("\n --------------------------------------------------------------------------------")
imp_customer.show_user_data()



# print("\n concesionario ...")
# print(f"Balance: {concessionaire1.balance}")
# concessionaire1.show_vehicles()

print("\n concesionario ...")
print(f"Balance: {concessionaire1.balance}")
concessionaire1.show_vehicles()

print("___________________________________________________________________________________")