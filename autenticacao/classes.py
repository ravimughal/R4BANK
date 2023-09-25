import database as db
import app

class Cliente():
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def show(self):
        print('cpf: ', self.cpf)
        print('nome: ', self.nome)

class Banco(Cliente):
    def __init__(self, cpf, nome):
        super().__init__(cpf, nome)
        self.saldo = 0
    
    def deposito(self, quantidade):
        self.quantidade = quantidade
        self.saldo = self.saldo + self.quantidade
        print("total R$", self.saldo)

    def saque(self, quantidade):
        self.quantidade = quantidade
        if (self.saldo < self.quantidade):
            print("saldo insuficiente")
            return 0

        self.saldo = self.saldo - self.quantidade
        print("total R$", self.saldo)

    def ver_saldo(self):
        print(self.saldo)

conn = db.connect_db()

get_name = db.search_user(conn)
