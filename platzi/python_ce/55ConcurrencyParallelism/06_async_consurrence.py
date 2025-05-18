import asyncio
import time
import random
import multiprocessing

#función asincrona para veridicar el inventario
async def check_inventory(item):
    try:
        # print("\n___________________________________________________________")
        print(f"verificando inventario para {item} ...")
        await asyncio.sleep(random.randint(3,6))
        print(f"inventario VERIFICADO para {item}")
        # print("___________________________________________________________")

        #simular disponibilidad del producto
        return random.choice([True, False, True, True])
    except Exception as ex:
        print(ex)

#función para procesar el pago
async def process_payment(order_id):
    try:
        # print("\n___________________________________________________________")
        print(f"Procesando pago para la orden [{order_id}] ...")
        #simular el tiempo de espera del servicio de pago
        await asyncio.sleep(random.randint(3,6))
        print(f"Pago procesado para la orden [{order_id}]")
        # print("___________________________________________________________")
        return True
    except Exception as ex:
        print(ex)

#Funcion intensiva en CPU para calcular el costo total del pedido
def calculate_total(items):
    try:
        # print("\n___________________________________________________________")
        print(f"Calculando costo total para {len(items)} articulos ...")
        time.sleep(5)
        total = sum(item['price'] for item in items)
        print(f"Costo total calculado: {total}")
        # print("___________________________________________________________")
        return total
    except Exception as ex:
        print(ex)

async def process_order(order_id, items):
    try:
        payment_result = False

        # print("\n___________________________________________________________")
        print(f"Iniciando el procesamiento de la orden [{order_id}] ...")
        #Verificar el inventario para cada articulo
        inventory_check = [check_inventory(item['name']) for item in items]  #este crea una lista de funciones a ejecutar
        inventory_results = await asyncio.gather(*inventory_check)  #este indica a asyncio la lista a ejecutar asincronamente

        print(f"fin check_inventory orden [{order_id}]")

        if not all(inventory_results):
            print(f"Orden [{order_id}] cancelada: Producto no está disponible")
        else:
            with multiprocessing.Pool() as pool:
                total = pool.apply(calculate_total, (items, )) #se ejecuta el proceso hasta que termine

            #Procesar el pago
            payment_result = await process_payment(order_id)

        if payment_result:
            print(f"\n🎉 Orden [{order_id}] completada con éxito. Total: {total}\n")
        else:
            # raise Exception(f"\n❌ Error al procesar el pago de la orden [{order_id}]\n")
            print(f"\n❌ Error al procesar el pago de la orden [{order_id}]\n")
        
        # print("___________________________________________________________")
        return total
    except Exception as ex:
        print(ex)

async def main():
    try:
        orders = [
            {'order_id': 1, 'items': [{'name': 'Laptop', 'price': 1000}, {'name': 'Mouse', 'price': 50}, {'name': 'Smartphone', 'price': 700}]},
            {'order_id': 2, 'items': [{'name': 'Teclado', 'price': 80}, {'name': 'Monitor', 'price': 300}]},
            {'order_id': 3, 'items': [{'name': 'Smartphone', 'price': 700}, {'name': 'Funda', 'price': 20}]}
        ]

        #Procesar múltiples órdenes concurrentemente
        tasks = [process_order(order['order_id'] , order['items']) for order in orders]
        await asyncio.gather(*tasks)
    except Exception as ex:
        print(ex)

#creamos el event loop
if __name__ == '__main__':
    asyncio.run(main())