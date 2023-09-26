import database
import classes
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

        cliente = classes.Cliente(nome, cpf)
        cliente.show()

    elif msg == 2:
        conn = database.connect_db()
        dados = cadastrar.cadastrar()
        if dados == -1:
            return dados
        database.create_user(conn, dados)
        return dados
    elif msg == 3:
        exit()

    return 1

while True:
    opt_res = opt()
    if opt_res == 3:
        break
