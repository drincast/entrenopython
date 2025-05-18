import asyncio

async def process_data(data):
    try:
        print(f"Procesando {data} ...")

        #simular una operacion
        await asyncio.sleep(10)
        print(F"{data} procesado!")
        return data * 2
    except Exception as ex:
        print(ex)

async def main():
    try:
        print("inicio de procesamiento")
        result = await process_data('archivo.txt')
        print("hola")
        print(f"Resultado {result}")
        print("adios")
    except Exception as ex:
        print(ex)

print("inicio")
asyncio.run(main())
print("fin")
asyncio.run(main())