import database
import classes
from cadastro import validacao_cpf


def principal_app(cliente_objeto):

    conn = database.connect_db()
    cpf = cliente_objeto.cpf

    app_comands = int(input("""
Selecione uma opção
1 - Ver Saldo
2 - Deposito 
3 - Sacar
4 - Transferencia
5 - Sair
"""))
    saldo = database.saldo(conn, cpf)
    cliente_objeto.saldo = saldo
    if app_comands == 1:

        cliente_objeto.ver_saldo()

    elif app_comands == 2:
        quantidade = float(input("Digite o valor a ser depositado: "))
        cliente_objeto.deposito(quantidade)

    elif app_comands == 3:
        quantidade = float(input("Digite o valor do saque: "))
        cliente_objeto.saque(quantidade)

    elif app_comands == 4:
        quantidade = float(input("Digite o valor da transferencia: "))
        chave = str(input("Digite o CPF de quem vai receber: "))
        chave = validacao_cpf.padronizando_cpf(chave)
        existe = database.procurar_cpf(conn, chave)

        print(chave, existe)

        if existe != chave:
            print("Digite um CPF válido")
            return 0

        nome_destinatario = database.procurar_nome(conn, chave)

        destinatario = classes.Banco(chave, nome_destinatario)
        cliente_objeto.transferencia(quantidade, destinatario)
    elif app_comands == 5:
        return 0