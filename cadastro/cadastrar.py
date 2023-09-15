from cadastro import requisicoes
from cadastro import erros
from cadastro import password_security
from cadastro import validacao_email
import database



def cadastrar():
    nome = requisicoes.nome()
    if nome == -1:
        return -1
    cpf = requisicoes.cpf()
    if cpf == -1:
        return -1

    cpf = str(cpf)

    conn = database.connect_db()
    exist = database.read_user(conn)

    if cpf in exist:
        erros.cpf_ja_cadastrado()
        return -1


    while True:
        email = requisicoes.email()
        if email == -1:
            return -1
        verificar = validacao_email.executar_verificacao_de_email(email)

        if verificar == 1:
            break
    
    
    validacao_email.email_cadastrado(email)

    while True:
        senha = requisicoes.senha()
        if senha == -1:
            return -1
        verificacao = password_security.executar_verificacoes_de_senha(senha)
        if verificacao == 1:
            break

    return cpf, email, nome, senha
    

if __name__ == '__main__':
    pass