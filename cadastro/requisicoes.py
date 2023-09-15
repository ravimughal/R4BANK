from cadastro import erros

def nome():
    while True:
        nome = input("Digite seu nome: ")
        if erros.sair(nome) == -1:
            return -1
        confirm = input(f"Nome está correto? {nome} (s / n): ")

        if confirm == 's':
            return nome            

def cpf():
    while True:
        cpf = input("Digite seu cpf: ")
        if erros.sair(cpf) == -1:
            return -1
        confirm = input(f"CPF está correto? {cpf} (s / n): ")

        if confirm == 's':
            return cpf

def email():
    while True:
        email = input("Digite seu email: ")
        if erros.sair(email) == -1:
            return -1
        confirm = input(f"Email está correto? {email} (s / n): ")

        if confirm == 's':
            return email

def senha():
    while True:
        senha = input("Digite sua senha: ")

        if erros.sair(senha) == -1:
            return -1
        confirm = input(f"Senha está correto? {senha} (s / n): ")

        if confirm == 's':
            return senha
        

if __name__ == '__main__':
    print("hello world")