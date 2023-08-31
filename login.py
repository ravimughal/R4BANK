import mysql.connector


def conect_db():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="r4 bank"
    )

    return conn


def read_user(conn):
    cursor = conn.cursor()
    comando = f'SELECT cpf FROM usuarios'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()

    return resultado


def read_password(conn, posicao):
    cursor = conn.cursor()
    comando = f'SELECT senha FROM usuarios'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()

    return resultado[posicao]

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

def serch_password():
    pass


def cpf_usuario(resultado):
    cpf = input("Digite o cpf: ")
    posicao = search_user(resultado, cpf)
    return posicao

def senha_usuario(senha_bd):
    senha = input("Digite a senha: ")
    
    if senha == senha_bd[0]:
        print("logado")
    
    return senha


def main():
    conn = conect_db()
    posicao = cpf_usuario(read_user(conn))
    senha_usuario(read_password(conn, posicao))
    conn.close()


if __name__ == '__main__':
    main()
