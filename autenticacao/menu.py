import database
from login import main
from cadastro import cadastrar


print("Bem vindo ao R4 BANK")


def opt():
    msg = input("""
Selecione uma opção: 
1 - Login
2 - Cadastrar
3 - Sair 
""")

    msg = int(msg)

    if msg == 1:
        main.main()
    elif msg == 2:
        conn = database.connect_db()
        dados = cadastrar.cadastrar()
        if dados == -1:
            return dados
        database.create_user(conn, dados)
    elif msg == 3:
        exit()

    return 1


while True:
    opt_res = opt()
    if opt_res == 3:
        break
