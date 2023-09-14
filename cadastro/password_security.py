def tamanho_da_senha(senha):
    if len(senha) >= 8:
        return 1
    return 0
    
def possui_caracteres_especiais(senha):
    caracteres_especiais = r"!@#$%^&*(),.?\":{}|<>"

    for caractere in senha:
        if caractere in caracteres_especiais:
            return 1
    return 0

def possui_numeros(senha):
    numeros = r'0123456789'

    for i in senha:
        if i in numeros:
            return 1
    return 0

def possui_letra(senha):
    for caractere in senha:
        if caractere.isalpha():
            return 1
    return 0

def executar_verificacoes_de_senha(senha):
    pre_requisos = 'A senha precisa de: \n'
    tamanho = tamanho_da_senha(senha)
    caracteres_especiais = possui_caracteres_especiais(senha)
    numeros = possui_numeros(senha)
    letras = possui_letra(senha)

    segura = True

    if tamanho == 0:
        pre_requisos += 'mais que 8 caracteres\n'
        segura = False

    if caracteres_especiais == 0:
        pre_requisos += 'caracteres especiais !@#$%^&*(),.?\":{}|<>' + '\n'
        segura = False

    if numeros == 0:
        pre_requisos += 'números \n'
        segura = False
    if letras == 0:
        pre_requisos += 'letras\n'
        segura = False

    if segura != True:
        print(pre_requisos)
        return 0
    else:
        return 1
    
if __name__ == '__main__':
    executar_verificacoes_de_senha('123')