import threading
import time

import threading

# Variable compartida
balance = 0
lock = threading.Lock()  # Crear un Lock

def deposit(money, transaction_id):
    global balance
    for _ in range(100000):
        with lock:  # Bloquear el acceso para evitar condiciones de carrera
            balance += money

    print(f"saldo: {balance} -- transacción: {transaction_id}")

def deposit_insecure(money, transaction_id):
    global balance

    print(f"iniciando transación {transaction_id}")
    
    for _ in range(100000):
        if transaction_id == 0 and _ == 7:
            # time.sleep(1)
            for _ in range(1000000):
                a = _
        balance += money

    print(f"saldo: {balance} -- transacción: {transaction_id}")

threads = []
for i in range(2):
    # thread = threading.Thread(target=deposit, args=(1,i))
    thread = threading.Thread(target=deposit_insecure, args=(1,i,))
    threads.append(thread)
    print(f"Ejecutando hilo id: {thread}")
    thread.start()

for thread in threads:
    thread.join()

print(f"Saldo final: {balance}")  # Esperamos ver 200000 como saldo