import re
import database

def verificar_email(email):
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$'

    if re.match(pattern, email):
        return 1
    else:
        return 0

def email_cadastrado(email):
    conn = database.connect_db()
    emails = database.read_email(conn)

    if email in emails:
        return 0
    else:
        return 1

def executar_verificacao_de_email(email):
    its_email = verificar_email(email)
    email_existente = email_cadastrado(email)

    if its_email == 0:
        print("insira um email valido!")
        return 0
    elif email_existente == 0:
        print("email ja cadastrado")
        return 0
    else:
        return 1


if __name__ == '__main__':
    email_cadastrado('ravi@hotmail.com')
