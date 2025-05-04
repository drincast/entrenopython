def log_transaction(func):
    def wrapper():
        print('1 Log de transacción ...')
        func()
        print('3 Log terminado !')

    return wrapper

@log_transaction
def process_payment():
    try:
        print('2 Procesando pago ...')
    except Exception as ex:
        print(ex)

process_payment()

