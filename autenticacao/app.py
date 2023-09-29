import database
import classes

def principal_app(cliente_objeto):
    conn = database.connect_db()
    cpf = cliente_objeto.cpf

    app_comands = int(input("""
Selecione uma opção
1 - Ver Saldo
2 - Deposito 
3 - Sacar
4 - Sair
"""))
    
    if app_comands == 1:
        saldo = database.saldo(conn, cpf)
        cliente_objeto.saldo = saldo
        cliente_objeto.ver_saldo()

    elif app_comands == 2:
        valor = float(input("Digite o valor a ser depositado: "))
        database.depositar(conn, cpf, valor)
        

    elif app_comands == 3:
        valor = float(input("Digite o valor do saque: "))