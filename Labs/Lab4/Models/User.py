from Models.Entity import *

class User(Entity):
    def __init__(self, id, login, password):
        self.id = id;
        self.login = login;
        self.password = password;


