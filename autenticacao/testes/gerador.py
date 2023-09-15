import random
import string

def gerar_nome():
    nome = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    return nome

def gerar_cpf():
    # Gera nove dígitos aleatórios
    cpf = [str(random.randint(0, 9)) for _ in range(9)]
    
    # Calcula os dois dígitos verificadores
    soma = 0
    for i, valor in enumerate(cpf):
        soma += int(valor) * (10 - i)
    primeiro_digito = 11 - (soma % 11)
    primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
    cpf.append(str(primeiro_digito))
    
    soma = 0
    for i, valor in enumerate(cpf):
        soma += int(valor) * (11 - i)
    segundo_digito = 11 - (soma % 11)
    segundo_digito = segundo_digito if segundo_digito <= 9 else 0
    cpf.append(str(segundo_digito))
    
    # Formata o CPF com zeros e traços
    cpf_formatado = "{}{}{}.{}{}{}.{}{}{}-{}{}".format(*cpf)
    
    return cpf_formatado


def gerar_email():
    dominios = ["gmail.com", "yahoo.com", "hotmail.com", "example.com", "outlook.com"]
    nome = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    dominio = random.choice(dominios)
    return f"{nome}@{dominio}"

