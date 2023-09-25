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



def read_email(conn):
    cursor = conn.cursor()
    comando = f'SELECT email FROM usuarios'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()

    emails = [tupla[0] for tupla in resultado]
    return emails


def read_password(conn, cpf):
    cursor = conn.cursor()
    comando = f'SELECT senha FROM usuarios WHERE cpf = %s'

    cursor.execute(comando, (cpf,))
    resultado = cursor.fetchone()
    cursor.close()

    print(resultado)

    return resultado

def id_user(conn):
    cursor = conn.cursor()
    comando = f'SELECT cpf FROM usuarios'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close

    return resultado


def create_user(conn, dados):
    cursor = conn.cursor()
    cpf = validacao_cpf.padronizando_cpf(dados[0])
    comando = f'INSERT INTO usuarios(cpf, email, nome, senha) VALUES("{cpf}", "{dados[1]}", "{dados[2]}", "{dados[3]}")'
    conta_table = f'INSERT INTO conta(cpf, nome,saldo, historico) VALUES("{cpf}","{dados[2]}","0", "0")'
    cursor.execute(comando)
    cursor.execute(conta_table)
    conn.commit()

def search_user(conn):
    cursor = conn.cursor()
    comando = f'SELECT cpf FROM conta'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    resultado = [tupla[0] for tupla in resultado]

    print(resultado)
    return resultado

if __name__ == '':
    conn = connect_db()
    create_user(conn, [f'{gerador.gerar_cpf()}', f'{gerador.gerar_email()}', f'{gerador.gerar_nome()}', 'teste123'])

if __name__ == '__main__':
    conn = connect_db()
    search_user(conn)