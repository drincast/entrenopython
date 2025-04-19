import logging
import traceback

import csv
import json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def file_txt_management():
    rows = 0
    with open("file001.txt", "r") as file:
        for lines in file:
            rows = len(file.readlines())
        
    print(f"El archivo tiene {rows} líneas")

    #Leer linea por linea
    # with open("file001.txt", "r") as file:
    #     for lines in file:
    #         print(lines.strip())

    #leer las lineas y guardarlas en una lista
    # with open("file001.txt", "r") as file:
    #     lines = file.readlines()
    #     print(lines)
    #     print(len(lines))

    #agregar en el archivo
    # with open("file001.txt", "a") as file:
    #     file.write("\n\nPython by ME")

    #escribir en el archivo
    # with open("file001.txt", "w") as file:
    #     file.write("\n\nPython by ME")
    pass

def file_csv_management(mode_file):
    if mode_file == "r":
        #modo lectura de csv
        with open("products.csv", mode="r") as file:
            csv_write = csv.DictReader(file)
            for row in csv_write:
                print(row)
    elif mode_file == "r_sc":
        #modo lectura de csv
        with open("products.csv", mode="r") as file:
            csv_write = csv.DictReader(file)
            for row in csv_write:
                print(f"Producto: {row['name']:20} ==>{'':3} Precio: {row['price']}")
    elif mode_file == "a_np":
        #agregar un nuevo producto
        new_product = {
            "name": "Wireless Charger",
            "price": 75,
            "quantity": 100,
            "brand": "ChargerMaster",
            "category": "Accessories",
            "entry_date": "2025-07-01"
        }

        with open("products.csv", mode="a", newline='') as file:
            file.write('\n') #necesario para que almacene en nueva linea del archivo
            csv_write = csv.DictWriter(file, fieldnames = new_product.keys())
            csv_write.writerow(new_product)
    elif mode_file == "update_products":
        file_path = "products.csv"
        update_file_path = "products_update.csv"

        #agregar un nuevo producto
        new_product = {
            "name": "Wireless Charger",
            "price": 75,
            "quantity": 100,
            "brand": "ChargerMaster",
            "category": "Accessories",
            "entry_date": "2025-07-01"
        }

        with open(file_path, mode="r") as file:
            csv_reader = csv.DictReader(file)
            #obtener nombre de las columnas
            # print(type(csv_reader.fieldnames), type(["total_value"]), csv_reader.fieldnames)
            columns_names = csv_reader.fieldnames + ["total_value"]

            print(type(csv_reader), csv_reader)

            with open(update_file_path, mode="w", newline="") as update_file:
                csv_write = csv.DictWriter(update_file, fieldnames = columns_names)
                csv_write.writeheader() #escribir en encabezado

                for row in csv_reader:
                    row["total_value"] = float(row["price"]) * int(row["quantity"])
                    print(type(row), row)
                    csv_write.writerow(row)

def file_json_management(mode_file):
    file_path = 'products.json'
    file_path_new = 'products_new.json'

    if(mode_file == 'r'):
        with open(file_path, mode="r") as file:
            products = json.load(file)

        print(type(products))

        for product in products:
            # print(product)
            print(f"Producto: {product['name']:20}=> {'':3}{product['price']}")    
    elif mode_file == "a_np":
        #agregar un nuevo producto
        new_product = {
            "name": "Wireless Charger",
            "price": 75,
            "quantity": 100,
            "brand": "ChargerMaster",
            "category": "Accessories",
            "entry_date": "2025-07-01"
        }

        with open(file_path, mode="r") as file:
            products = json.load(file)

        products.append(new_product)
        print('new_product', type(new_product), type(products), products)

        with open(file_path_new, mode="w") as file:
            json.dump(products, file, indent=4)

def simple_convert_csv_to_json(csv_file, json_file):
    try:
        values_list = []

        with open(csv_file, mode='r') as file:
            csv_read = csv.DictReader(file)

            for row in csv_read:
                values_list.append(row)

        with open(json_file, mode='w') as file:
            json.dump(values_list, file, indent=4)
    except Exception as ex:
        print(ex)

def simple_convert_json_to_csv(json_file, csv_file):
    try:
        #leer el json
        #leer el primer elemento, sacar los keys
        #convertir keys a lista con titulos de columnas
        #recorrer el json (list) para al macenarlo en diccionario
        #almacenar csv

        products = []
        columns_headers = []

        with open(json_file, mode='r') as file:
            products = json.load(file)

        products = []
        if len(products) <= 0:
            raise  Exception("El archivo no tiene datos, reviselo por favor.")
        
        print(type(products), products[0], list(products[0].keys()))
        
        columns_headers = list(products[0].keys())

        with open(csv_file, mode="w", newline="") as to_csv_file:
            csv_write = csv.DictWriter(to_csv_file, fieldnames = columns_headers)
            csv_write.writeheader() #escribir en encabezado

            for row in products:
                    print(type(row), row)
                    csv_write.writerow(row)
    except Exception as ex:
        # print(ex)
        # print(traceback.format_exc())
        logger.exception("Ocurrió una excepción")

#file_txt_management
# file_csv_management("update_products")
# file_json_management("a_np")
simple_convert_csv_to_json("products.csv", "result_json.json")
simple_convert_json_to_csv("products.json", "result_csv.csv")

