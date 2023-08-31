import mysql.connector

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
    return resultado

def read_password(conn, posicao):
    cursor = conn.cursor()
    comando = f'SELECT senha FROM usuarios'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    return resultado[posicao]
