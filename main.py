from autenticacao import database 

class Cliente:
    def __init__(self, nome):
        self.name = nome


print(database.id_user(database.connect_db()))
