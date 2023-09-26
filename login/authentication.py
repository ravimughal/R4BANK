def search_user(resultado, cpf):
    cont = 0
    for i in resultado:
        if i == cpf:
            print("CPF encontrado")
            return cont
        cont += 1
    print("CPF não encontrado")
    return -1


def cpf_usuario(resultado):
    cont = 0
    cpf = ''
    while True:
        cpf = input("Digite o CPF: ")
        posicao = search_user(resultado, cpf)

        cont += 1
        if posicao != -1:
            return cpf
        elif cont >= 3:
            print("Cadastre-se")
            break
    return posicao


def senha_usuario(senha_bd):
    cont = 0
    while True:
        senha = input("Digite a senha: ")

        cont += 1
        if senha == senha_bd:
            print("Logado")
            return 1 
        else:
            print("Senha incorreta")
            if cont >= 3:
                return 0


if __name__ == '__main__':
    senha_usuario('123')