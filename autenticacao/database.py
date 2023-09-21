import mysql.connector
from cadastro import validacao_cpf
from testes import gerador

def connect_db():
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

    # extrair strings das tuplas
    cpf = [tupla[0] for tupla in resultado]
    return cpf

def id_user(conn):
    cursor = conn.cursor()
    comando = f'SELECT id FROM usuarios'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close

    id = [tupla[0] for tupla in resultado]
    return id

def read_email(conn):
    cursor = conn.cursor()
    comando = f'SELECT email FROM usuarios'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()

    emails = [tupla[0] for tupla in resultado]
    return emails


def read_password(conn, posicao):
    cursor = conn.cursor()
    comando = f'SELECT senha FROM usuarios'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    return resultado[posicao]


def create_user(conn, dados):
    cursor = conn.cursor()
    cpf = validacao_cpf.padronizando_cpf(dados[0])
    comando = f'INSERT INTO usuarios(cpf, email, nome, senha) VALUES("{cpf}", "{dados[1]}", "{dados[2]}", "{dados[3]}")'
    cursor.execute(comando)
    conn.commit()


if __name__ == '__main__':
    conn = connect_db()
    create_user(conn, [f'{gerador.gerar_cpf()}', f'{gerador.gerar_email()}', f'{gerador.gerar_nome()}', 'teste123'])
