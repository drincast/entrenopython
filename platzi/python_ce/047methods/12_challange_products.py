import random
#Clase Producto, implementar validación de precio y stock no negativo
#Eliminar la informacion con la propiedad

class Product:
    def __init__(self, name: str, price: int, stock: int):
        try:
            self.name = name
            self._price = price
            self._stock = stock
        except Exception as ex:
            print(ex)

    @property
    def price(self):
        try:
            return self._price
        except Exception as ex:
            print(ex)

    @price.setter
    def price(self, new_price: int):
        try:
            if new_price < 0:
                raise ValueError(f"el precio del producto {self.name} no de debe ser negativo")
            
            self._price = new_price
        except Exception as ex:
            print(ex)

    @price.deleter
    def price(self):
        del self._price

    @property
    def stock(self):
        try:
            return self._stock
        except Exception as ex:
            print(ex)

    @stock.setter
    def stock(self, new_stock: int):
        try:
            if new_stock < 0:
                raise ValueError(f"la cantidad del producto {self.name} no de debe ser negativo")
            
            self._stock = new_stock
        except Exception as ex:
            print(ex)

    @stock.deleter
    def stock(self):
        del self._stock

    def show_product(self):
        try:
            print(f"Producto: {self.name} - precio: {self.price} - cantidad: {self.stock}")
        except Exception as ex:
            print(ex)

#general methods
def convert_to_obj_product(product: dict, max_stock: int):
    '''
    Description: realiza la conversion de datos a un objeto de Product, ademas asigna una cantidad seudoaleatoria
    '''
    try:
        stock = random.choice(range(1,max_stock + 1))
        obj_product = Product(product["name"], product["price"], stock)

        return obj_product
    except Exception as ex:
        print(ex)

#una lista de productos, convertiremos cada producto a un objeto de 
#clase Product
products_lst = [
    {'name' :'Smartphone Galaxy S23 Ultra', 'price': 1299}
    ,{'name' :'Tablet iPad Pro 12.9"', 'price':1199}
    ,{'name' :'Laptop MacBook Air M2', 'price':1099}
    ,{'name' :'Auriculares inalámbricos Sony WF-1000XM4', 'price':249}
    ,{'name' :'Smartwatch Apple Watch Series 8', 'price':499}
    ,{'name' :'Cámara DSLR Canon EOS 5D Mark IV', 'price':2499}
    ,{'name' :'Televisor OLED LG CX 55"', 'price':1299}
    ,{'name' :'Consola PlayStation 5', 'price':499}
    ,{'name' :'Consola Xbox Series X', 'price':499}
    ,{'name' :'Monitor 4K 27"', 'price':349}
    ,{'name' :'Altavoz inteligente Amazon Echo Dot (4ª generación)', 'price':49}
    ,{'name' :'Disco duro externo SSD Samsung T7', 'price':119}
    ,{'name' :'Teclado mecánico Logitech G Pro X', 'price':149}
    ,{'name' :'Ratón inalámbrico Logitech MX Master 3', 'price':99}
    ,{'name' :'Router Wi-Fi 6 TP-Link Archer AX6000', 'price':199}
    ,{'name' :'Cámara de seguridad IP Wyze Cam v3', 'price':49}
    ,{'name' :'Proyector 4K BenQ HT3550', 'price':899}
    ,{'name' :'Sistema de sonido envolvente 5.1 Sony HT-G700', 'price':499}
    ,{'name' :'Reproductor de Blu-ray 4K Sony UBP-X800M2', 'price':249}
    ,{'name' :'Lámpara de escritorio inteligente Philips Hue', 'price':79}
]

product_inventory = []

for item in products_lst:
    product_inventory.append(
        convert_to_obj_product(item, 20)
    )

print("---- INVENTARIO ----")

for item in product_inventory:
    item.show_product()

index = random.choice(range(1,21))

print("\n---- Modificando Producto ----")
product_inventory[index].show_product()
print('modificando')
product_inventory[index].price = -10
product_inventory[index].stock = -5
product_inventory[index].price = 1000
product_inventory[index].stock = 50
print("modificado")
product_inventory[index].show_product()
del product_inventory[index].price
product_inventory[index].show_product()
del product_inventory[index].stock
product_inventory[index].show_product()

