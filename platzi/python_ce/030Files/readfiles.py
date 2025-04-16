import csv

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
            columns_names = csv_reader.fieldnames + ["total_value"]

            with open(update_file_path, mode="w", newline="") as update_file:
                csv_write = csv.DictWriter(update_file, fieldnames = columns_names)
                csv_write.writeheader() #escribir en encabezado

                for row in csv_reader:
                    row["total_value"] = float(row["price"]) * int(row["quantity"])
                    csv_write.writerow(row)


file_csv_management("update_products")

