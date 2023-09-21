import database
from login import authentication

def main():
    conn = database.connect_db()
    resultado = database.read_user(conn)
    posicao = authentication.cpf_usuario(resultado)

    if posicao >= 1:
        senha = database.read_password(conn, posicao)
        sucess = authentication.senha_usuario(senha)
        id_user = database.id_user(conn, posicao)

        conn.close()

        print(id_user)
        return sucess
    
    return 0


if __name__ == '__main__':
    while True:
        login = main()
        if login == 1:
            break
