from datetime import datetime

class User:
    def __init__(self, user, email, password, active, creation_date):
        self.user = user
        self.email = email
        self.password = password
        self.is_active = active
        self.creation_date = creation_date

    def __repr__(self):
        return f"User(user='{self.user}', email='{self.email}', password='***')"

    def set_user(self, user, email, password, active):
        self.user = user
        self.email = email
        self.password = password
        self.is_active = active

        #el sistema debe asignar la fecha de creacion
        #self.creation_date = creation_date

    def print_user_info():
        pass

    def set_user(self, user, email, password, active, creation_date):
        try:
            if(self.user != ''):
                self.user = user
            else:
                raise Exception("El valor de user no puede ser vacio")
            
            if(self.email != ''):
                self.email = email
            else:
                raise Exception("El email no puede ser vacio")
            
            if(self.is_active != None):
                self.is_active = active
            else:
                raise Exception("Debe indicar si el usuario esta activo o no")
            
            if(self.password != ''):
                self.password = password
            else:
                raise Exception("El password no puede ser vacio")
            
            if(self.creation_date != ''):
                self.creation_date = creation_date
            else:
                raise Exception("Falta especificar la fecha de creación del usuario")           
            
        except Exception as ex:
            print("Error sistema: ", ex)

user = User('test', 'test@test', 'lacontraseña', True, datetime.now())

print(user)
print(user.password)