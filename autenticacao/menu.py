import database
import classes
import app
from login import main
from cadastro import cadastrar


print("Bem vindo ao R4 BANK")

dados = []

def opt():
    msg = input("""
Selecione uma opção: 
1 - Login
2 - Cadastrar
3 - Sair 
""")

    msg = int(msg)

    if msg == 1:
        cpf_nome = main.main()
        cpf = cpf_nome[0]
        nome = cpf_nome[1]

        cliente = classes.Banco(nome, cpf)


        if cpf and nome:
            return [1, cliente]

    elif msg == 2:
        conn = database.connect_db()
        dados = cadastrar.cadastrar()
        if dados == -1:
            return dados
        database.create_user(conn, dados)
        return dados
    elif msg == 3:
        return 3

    return 1

def bank(nome, cpf):
    app.inserir_nome_cpf(nome, cpf)

while True:
    opt_res = opt()
    if opt_res[0] == 1:
        cliente_objeto = opt_res[1]
        while True:
            app.principal_app(cliente_objeto)

    elif opt_res[0] == 3:
        break



if __name__ == '__main__':
    pass