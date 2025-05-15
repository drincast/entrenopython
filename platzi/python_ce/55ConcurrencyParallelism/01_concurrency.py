import threading
import time

#función que simula el procesamiento de una solicitud
def process_request(request_id):
    try:
        ts = 3 if request_id != 0 else 4
        print(f"Procesando solicitud {request_id}")
        time.sleep(ts)
        print(f"solicitud {request_id} completada")
    except Exception as ex:
        print(ex)

threads = []

for i in range(3):
    #crea nuevo hilo que ejecutará la función
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()
#esperar a que todos los hilos terminen
for thread in threads:
    #asegurar de el programa espere a que cada hilo termine
    thread.join()

print("Todas las solicitudes ejecutadas")