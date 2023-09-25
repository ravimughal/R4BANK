import database
from login import authentication

def main():
    conn = database.connect_db()
    resultado = database.read_user(conn)
    cpf = authentication.cpf_usuario(resultado)

    if int(cpf) >= 1:
        senha = database.read_password(conn, cpf)
        sucess = authentication.senha_usuario(senha)
        conn.close()

        print('cpf', cpf)
        if sucess == 1:
            pass
        return sucess
    
    return 0

if __name__ == '__main__':
    while True:
        login = main()
        if login == 1:
            break
