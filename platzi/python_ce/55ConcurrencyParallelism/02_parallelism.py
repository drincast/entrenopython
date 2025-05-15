import multiprocessing
import time

#función que calcule el cuadrado de un número

def calculate_square(n):
    try:
        print(f'cuadrado de {n}')
        if n == 3:
            time.sleep(1)
        return n*n
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    numbers = [1,2,3,4,5,6,7]

    #creamos un pool de procesos
    with multiprocessing.Pool() as pool:
        result = pool.map(calculate_square, numbers)

    print(f"Resultados: {result}")