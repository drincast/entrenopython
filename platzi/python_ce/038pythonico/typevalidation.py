def divide(a:int, b: int) -> float:
    try:
        #validar que los valores sean enteros

        if not isinstance(a,int) or not isinstance(b, int):
            raise TypeError('Error: los valores deben ser enteros o flotantes')
        
        if b == 0:
            raise ValueError('Error: el divisor no debe ser 0')
        
        return a/b
    except Exception as ex:
        print(ex)

resultado = divide(10, '2')   
resultado = divide(10, 0)
resultado = divide(10, 2)

print(resultado)