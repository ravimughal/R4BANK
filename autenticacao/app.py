import classes

def principal_app(cliente_objeto):

    cliente_objeto.show()

    app_comands = str(input("""
Selecione uma opção
1 - Ver Saldo
2 - Deposito 
3 - Sacar
"""))


def inserir_nome_cpf(nome, cpf):
    print(nome, cpf)
    return nome, cpf


if __name__ == '__main__':
    inserir_nome_cpf('ravi', '123')