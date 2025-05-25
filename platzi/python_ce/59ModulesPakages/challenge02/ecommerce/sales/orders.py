def set_order(product):
    try:
        print(f"Se a agregado la order de {product[1]} unidades de {product[0]}.")
    except Exception as ex:
        print(ex)
