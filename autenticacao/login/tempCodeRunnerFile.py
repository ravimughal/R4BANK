def create_user(conn, cpf, email, nome, senha):
    cursor = conn.cursor()
    comando =  f'INSERT INTO usuarios (cpf, email, nome, senha) VALUES ("{cpf}", "{email}", "{nome}", "{senha}")'
    cursor.execute(comando)
    conn.commit()


if __name__ == '__main__':
    conn = connect_db()
    create_user(conn, 123, 'ravi@hotmail.com', 'ravi', 'teste123')
