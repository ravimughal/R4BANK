import database
from login import app
from login import authentication

def main():
    conn = database.connect_db()
    resultado = database.read_user(conn)
    posicao = authentication.cpf_usuario(resultado)

    if int(posicao) >= 1:
        senha = database.read_password(conn, posicao)
        sucess = authentication.senha_usuario(senha)
        id_user = database.id_user(conn, posicao)

        conn.close()

        print(posicao)
        if sucess == 1:
            app.main()       
        return sucess
    
    return 0

if __name__ == '__main__':
    while True:
        login = main()
        if login == 1:
            break
