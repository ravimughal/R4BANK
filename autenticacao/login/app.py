import classes
import database

def main(posicao):
    conn = database.connect_db()
    users = database.search_user(conn)

    print(posicao)


