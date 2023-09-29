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
        print("total R$", float(self.saldo))
        conn = db.connect_db()
        db.atualizar_saldo(conn, self.cpf, self.saldo)

    def saque(self, quantidade):
        self.quantidade = quantidade
        if (self.saldo < self.quantidade):
            print("saldo insuficiente")
            return 0

        self.saldo = self.saldo - self.quantidade
        print("total R$", float(self.saldo))
        conn = db.connect_db()
        db.atualizar_saldo(conn, self.cpf, self.saldo)

    def ver_saldo(self):
        print(f"o saldo é de R${self.saldo}")


if __name__ == '__main__':

    conn = db.connect_db()

    db.saldo(conn, '12712582349')

    usuario = Cliente()