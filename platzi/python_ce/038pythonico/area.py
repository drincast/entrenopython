def calculate_area(base, height):
    """
    Calcula el área de un triángulo
    """
    try:
        return (base * height) / 2
    except Exception as ex:
        print(ex)