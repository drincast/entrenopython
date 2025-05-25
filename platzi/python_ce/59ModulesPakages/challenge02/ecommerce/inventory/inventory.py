#agrega un producto al inventario
def add_product(product_name, stock):
    try:
        print(f"Producto {product_name} agregando con {stock} unidades")
    except Exception as ex:
        print(ex)

def remove_producto(product_name):
    try:
        print(f"Producto {product_name} eliminado del inventario.")
    except Exception as ex:
        print(ex)