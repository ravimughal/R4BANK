import classes

def principal_app(cliente):
    cliente.show()

def inserir_nome_cpf(nome, cpf):
    print(nome, cpf)
    return nome, cpf


if __name__ == '__main__':
    inserir_nome_cpf('ravi', '123')