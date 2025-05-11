class MultiplierFactory:
    def __new__(cls, factor: int):
        print(f"Creando instancia con factor {factor}, {cls}")
        return super(MultiplierFactory, cls).__new__(cls)
    
    def __init__(self, factor: int):
        print(f"Inicializando con factor {factor}")
        self.factor = factor    
    
    def __call__(self, number: int) -> int:
        print(f"Realizando multiplicación")
        return number * self.factor

# ejecuta primero __new__ y luego __init__
multiplier = MultiplierFactory(5)

#ejecuta __call__
result = multiplier(10)
print(result)