from cadastro import requisicoes

def cadastrar():
    nome = requisicoes.nome()
    cpf = requisicoes.cpf()
    email = requisicoes.email()
    senha = requisicoes.senha()

    return cpf, email, nome, senha
    

if __name__ == '__main__':
    pass