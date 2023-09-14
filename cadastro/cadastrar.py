from cadastro import requisicoes
from cadastro import erros
from cadastro import password_security
import database

def cadastrar():
    nome = requisicoes.nome()
    cpf = requisicoes.cpf()
    cpf = str(cpf)

    conn = database.connect_db()
    exist = database.read_user(conn)

    if cpf in exist:
        erros.cpf_ja_cadastrado()
        return -1

    email = requisicoes.email()

    while True:
        senha = requisicoes.senha()
        verificacao = password_security.executar_verificacoes_de_senha(senha)
        if verificacao == 1:
            break

    return cpf, email, nome, senha
    

if __name__ == '__main__':
    pass