def nome():
    while True:
        nome = input("Digite seu nome: ")
        confirm = input(f"Nome está correto? {nome} (s / n): ")

        if confirm == 's':
            return nome            

def cpf():
    while True:
        cpf = input("Digite seu cpf: ")
        confirm = input(f"CPF está correto? {cpf} (s / n): ")

        if confirm == 's':
            return cpf

def email():
    while True:
        email = input("Digite seu email: ")
        confirm = input(f"Email está correto? {email} (s / n): ")

        if confirm == 's':
            return email

def senha():
    while True:
        senha = input("Digite sua senha: ")
        confirm = input(f"Senha está correto? {senha} (s / n): ")

        if confirm == 's':
            return senha
        

if __name__ == '__main__':
    print("hello world")