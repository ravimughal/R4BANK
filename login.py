import mysql.connector


def conect_db():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="r4 bank"
    )

    return conn


def read(conn):
    cursor = conn.cursor()
    comando = f'SELECT cpf FROM  usuarios'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()

    print(resultado)
    return resultado


def search_user(resultado, cpf):
    cont = 0
    for i in resultado:
        # o resultado é retornado como uma sequencia de tuplas, por isso a necessidade do [0]
        if i[0] == cpf:
            print("ok")
            return cont

        cont += 1
    
    print("CPF não encontrado")
    return -1


def cpf_usuario(resultado):
    cpf = input("Digite o cpf: ")

    search_user(resultado, cpf)

    return cpf


def senha_usuario():
    senha = input("Digite a senha: ")

    return senha


def main():
    conn = conect_db()
    cpf_usuario(read(conn))
    conn.close()


if __name__ == '__main__':
    main()
