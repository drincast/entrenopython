#Proces la venta
def process_sale(product_name, quantity):
    try:
        print(f"Venta procesada: {quantity} unidades de {product_name}")
    except Exception as ex:
        print(ex)