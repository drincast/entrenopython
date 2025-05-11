class BaseClass:
    def __init__(self):
        try:
            self._protected_variable = 'Protected'
            self.__private_variable = 'Private'
            self.public_varible = 'Public'

        except Exception as ex:
            print(ex)

    def _protected_method(self):
        try:
            print('Este método es protegido')
        except Exception as ex:
            print(ex)

    def __private_method(self):
        try:
            print('Este método es privado')
        except Exception as ex:
            print(ex)

    def public_method(self):
        try:
            print('llamamos al método privado desde el método publico')
            self.__private_method()
        except Exception as ex:
            print(ex)

base = BaseClass()

print("\natributo y método publicos")
print(base.public_varible)
base.public_method()

print("\natributo y método protegidos")
print(base._protected_variable)
base._protected_method()

print("\natributo y método privados")
print(base.__private_variable)
base.__private_method()

