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


# Função para criar uma conexão sem um banco de dados específico
def connect_no_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    return conn

# Função para criar o banco de dados e tabelas


def criar_banco_e_tabelas(conn):
    try:
        # Verifica se a conexão está ativa
        if conn.is_connected():
            # Cria o cursor para executar comandos SQL
            cursor = conn.cursor()

            # Cria o banco de dados se não existir
            cursor.execute("CREATE DATABASE IF NOT EXISTS `r4 bank`")

            # Usa o banco de dados
            cursor.execute("USE `r4 bank`")

            # Cria a tabela `usuarios` se não existir
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS `usuarios` (
                    `id` INT AUTO_INCREMENT PRIMARY KEY,
                    `cpf` VARCHAR(11),
                    `email` VARCHAR(255) NOT NULL,
                    `nome` VARCHAR(20) NOT NULL,
                    `senha` VARCHAR(20) NOT NULL
                )
            """)

            # Cria a tabela `conta` se não existir
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS `conta` (
                    `cpf` VARCHAR(11) PRIMARY KEY,
                    `nome` VARCHAR(256) NOT NULL,
                    `saldo` FLOAT NOT NULL DEFAULT 0,
                    `historico` LONGTEXT CHECK (JSON_VALID(`historico`))
                )
            """)

            # Confirma as alterações no banco de dados
            conn.commit()

            print("Banco de dados e tabelas criados com sucesso.")

            # Fecha o cursor
            cursor.close()
    except mysql.connector.Error as err:
        print(f"Erro ao criar banco de dados e tabelas: {str(err)}")
    finally:
        if conn.is_connected():
            # Fecha a conexão se estiver aberta
            conn.close()


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
    comando = f'SELECT nome, senha FROM usuarios WHERE cpf = %s'

    cursor.execute(comando, (cpf,))
    resultado = cursor.fetchone()
    cursor.close()

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
    comando = f'SELECT cpf FROM conta WHERE cpf'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    resultado = [tupla[0] for tupla in resultado]

    print(resultado)
    return resultado


def saldo(conn, cpf):
    cursor = conn.cursor()
    comando = f'SELECT saldo FROM conta WHERE cpf = {cpf}'
    cursor.execute(comando)
    resultado = cursor.fetchone()
    cursor.close()

    resultado = resultado[0]
    return resultado


def atualizar_saldo(conn, cpf, saldo):
    cursor = conn.cursor()
    comando = f'UPDATE conta SET saldo = {saldo} WHERE cpf = {cpf}'
    cursor.execute(comando)
    conn.commit()


def procurar_cpf(conn, cpf):
    cursor = conn.cursor()
    comando = f'SELECT cpf FROM conta WHERE cpf = {cpf}'
    cursor.execute(comando)
    resultado = cursor.fetchone()
    cursor.close()

    resultado = resultado[0]
    print(resultado)
    return resultado


def procurar_nome(conn, cpf):
    cursor = conn.cursor()
    comando = f'SELECT nome FROM conta WHERE cpf = {cpf}'
    cursor.execute(comando)
    resultado = cursor.fetchone()
    cursor.close()

    resultado = resultado[0]
    print(resultado)
    return resultado


if __name__ == '':
    conn = connect_db()
    create_user(conn, [f'{gerador.gerar_c80if()}',
                f'{gerador.gerar_email()}', f'{gerador.gerar_nome()}', 'teste123'])

if __name__ == '__main__':
    conn = connect_db()
    procurar_nome(conn, '15304307127')
