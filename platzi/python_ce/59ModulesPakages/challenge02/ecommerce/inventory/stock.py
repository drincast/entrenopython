def get_stock(product):
    try:
        print(f"{product[1]} unidades de {product[0]}.")
    except Exception as ex:
        print(ex)

