import multiprocessing
import multiprocessing.queues
import time

#función que calcule el cuadrado de un número

def calculate_square(numbers, queue, id_process):
    try:
        # if n == 3:
        #     time.sleep(1)

        print(type(queue))

        for n in numbers:
            print(f'insertando cuadrado de {n}')
            # queue.put(n*n)
            if isinstance(queue, multiprocessing.queues.Queue):
                queue.put(n*n)
            else:
                queue.append(n*n)

        print(f"en {id_process} proceso queue = {queue}")
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    numbers = [1,2,3,4,5,6,7]
    queue = [] 
    queue2 = multiprocessing.Queue()

    # #creamos un pool de procesos
    # with multiprocessing.Pool() as pool:
    #     result = pool.map(calculate_square, numbers)

    second_process = multiprocessing.Process(target=calculate_square, args=(numbers, queue, 'segundo'))
    second_process.start()
    second_process.join()

    third_process = multiprocessing.Process(target=calculate_square, args=(numbers, queue2, 'tercero'))
    third_process.start()
    third_process.join()

    print(f"en primer proceso queue = {queue}")
    print(f"en primer proceso queue2 = {queue2}")

    # while not queue.empty():
    while len(queue) > 0:
        print(queue.get())

    while not queue2.empty():
        print(queue2.get())