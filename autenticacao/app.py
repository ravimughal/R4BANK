import database

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
        print(f"O saldo da conta é: {saldo}")

    elif app_comands == 2:
        depositar()




def depositar():
    print("depositei")


def inserir_nome_cpf(nome, cpf):
    print(nome, cpf)
    return nome, cpf


if __name__ == '__main__':
    inserir_nome_cpf('ravi', '123')