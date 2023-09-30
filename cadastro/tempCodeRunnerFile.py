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
        print("usuario ja cadastrado")
    else:
        print("nao cadastrado")


if __name__ == '__main__':
    email_cadastrado('ravi@hotmail.com')
