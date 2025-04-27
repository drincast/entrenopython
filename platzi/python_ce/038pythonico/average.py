def calculate_average(numbers):
    """
    Calcula el promedio de una lista de números
    Parameters
        numbers (list): lista de números enteros o flotantes

    returns:
        float: promedio de los números de una lista
    """    
    try:
        return sum(numbers) / len(numbers)
    except Exception as ex:
        print(ex)

# imprimiendo el resultado de la funcion
print(calculate_average([1,2,3,4,5]))