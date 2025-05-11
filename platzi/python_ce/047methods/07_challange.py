#reto funcion que recibe una cantidad variable de productos y sus precios
#calcula el total y aplique un descuento opcional si se proporciona
#como argumento con nombre

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

discounts_lst = [
    {'discount_name' :'Black Friday', 'discount_percent': 0.2}
    ,{'discount_name' :'Navidad', 'discount_percent': 0.15}
    ,{'discount_name' :'Verano', 'discount_percent': 0.1}
    ,{'discount_name' :'Cyber Monday', 'discount_percent': 0.25}
    ,{'discount_name' :'Día del Padre', 'discount_percent': 0.1}
    ,{'discount_name' :'Día de la Madre', 'discount_percent': 0.15}
    ,{'discount_name' :'Black Friday', 'discount_percent': 0.2}
    ,{'discount_name' :'Navidad', 'discount_percent': 0.1}
    ,{'discount_name' :'Cyber Monday', 'discount_percent': 0.15}
    ,{'discount_name' :'Verano', 'discount_percent': 0.1}
    ,{'discount_name' :'Día del Padre', 'discount_percent': 0.2}
]

def calculate_total(*args, discount_name, discount_percent):
    '''
    Description: calcula el total de la venta
    Parameters:
        *args: los productos
        **kwargs: un descuento
    Returs: El total de la venta
    '''

    try:
        total_not_discount = 0
        discount = 0
        total = 0

        for products in args:
            for product in products:
                total_not_discount = total_not_discount + product['price']

        if discount_percent is not None:
            discount = total_not_discount * discount_percent

        total = total_not_discount - discount

        print(f"El total es {total_not_discount}")
        print(f"Se realizo un descuento {discount_name} de {discount}")
        print(f"total de la venta {total}")

        return total
    except Exception as ex:
        print(ex)

calculate_total(products_lst, **discounts_lst[3])