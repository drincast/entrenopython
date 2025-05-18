import asyncio
import random
import time

async def download_data(data):
    try:
        waiting = ""
        print(f"Descargando {data} [asincrono]")

        time_download = random.choice(range(1,10))

        for t in range(time_download):
            # waiting = waiting + "."
            print(".", end="", flush=True)
            #simula espera de descarga
            await asyncio.sleep(1)
            # time.sleep(1)

        print(F"\n{data} descargado!")
        return f"espera de {time_download}s"
    except Exception as ex:
        print(ex)

async def main():
    try:
        print("inicio de descarga")
        result = await download_data('archivo.txt')
        print(f"Resultado {result}")
    except Exception as ex:
        print(ex)

def n_download_data(data):
    try:
        waiting = ""
        print(f"Descargando {data}")

        time_download = random.choice(range(1,10))

        for t in range(time_download):
            # waiting = waiting + "."
            print(".", end="", flush=True)
            #simula espera de descarga
            time.sleep(1)

        print(F"\n{data} descargado!")
        return f"espera de {time_download}s"
    except Exception as ex:
        print(ex)

def n_main():
    try:
        print("inicio de descarga")
        result = n_download_data('archivo.txt')
        print(f"Resultado {result}")
    except Exception as ex:
        print(ex)

asyncio.run(main())
print()
n_main()
