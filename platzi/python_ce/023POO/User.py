class User:
    def __init__(self, user, email, password, active, creation_date):
        self.user = user
        self.email = email
        self.password = password
        self.is_active = active
        self.creation_date = creation_date