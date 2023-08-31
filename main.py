import database
import authentication

def main():
    conn = database.connect_db()
    resultado = database.read_user(conn)
    posicao = authentication.cpf_usuario(resultado)
    senha = database.read_password(conn, posicao)
    authentication.senha_usuario(senha)
    conn.close()

if __name__ == '__main__':
    main()
