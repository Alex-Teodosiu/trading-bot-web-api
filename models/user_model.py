class User:
    def __init__(self, email, password, id=None):
        self._id = id
        self._email = email
        self._password = password

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    def to_dict(self):
        return {
            'id': self.get_id(),
            'email': self.get_email(),
            'password': self.get_password()
        }

    def __str__(self):
        return f"ID: {self._id}, Email: {self._email}, Password: {self._password}"