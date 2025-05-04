class Calculator:
    count = 0

    def __init__(self, radius: float = None):
        self._radius = radius
    
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b
    
    @classmethod
    def counter_increment(cls):
        try:
            cls.count += 1
        except Exception as ex:
            print(ex)

    @property
    def area_circle_calculator(self) -> float:
        return 3.1416 * (self._radius **2)
    
    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, value: float):
        if value < 0:
            raise ValueError("El radio debe ser mayor a o igual cero")
        self._radius = value

print(Calculator.count)
Calculator.counter_increment()
Calculator.counter_increment()
print(Calculator.count)

print(Calculator.add(3, 9))

circle = Calculator(5)
print(circle.area_circle_calculator)
circle.radius = 10
print(circle.area_circle_calculator)
