from cadastro import requisicoes
from cadastro import erros
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
    senha = requisicoes.senha()

    return cpf, email, nome, senha
    

if __name__ == '__main__':
    pass