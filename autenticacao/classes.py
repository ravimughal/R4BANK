import database as db

class Cliente:
    def __init__(self, nome, id):
        self.id = id
        self.nome = nome


conn = db.connect_db()

dados_cliente = Cliente("Ravi", 15)
