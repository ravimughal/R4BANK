import re


def validacao_cpf(cpf):
    padronizando = padronizando_cpf(cpf)
    comprimento = comprimento_cpf(padronizando)
    if comprimento == -1:
        return -1
    verificando = verificando_cpf(comprimento)
    if verificando == 1:
        return cpf
    else:
        return 0    

def comprimento_cpf(cpf):
    tamanho = len(cpf)
    if tamanho == 11:
        return cpf
    else:
        return -1

def padronizando_cpf(cpf):
    cpf_formatado = ''
    for i in cpf:
        if i.isdigit():
            cpf_formatado += i

    cpf = cpf_formatado
    return cpf


def verificando_cpf(cpf):
    def calcular_digito_verificador(total, posicao_digito_verificador):
        digito_verificador = 0
        digito_verificador = total % 11

        if digito_verificador in (0, 1):
            digito_verificador = 0
        else:
            digito_verificador = 11 - digito_verificador

        digito_verificador = str(digito_verificador)
        if posicao_digito_verificador == '1':
            if cpf[9] == digito_verificador:
                return 1
            else: 
                return 0
        elif posicao_digito_verificador == '2':
            if cpf[10] == digito_verificador:
                return 1
            else:
                return 0
    def primeiro_verificador():
        total = 0
        multiplicador = 10
        for i in range(9):
            total += int(cpf[i]) * multiplicador
            multiplicador -= 1
        verificado = calcular_digito_verificador(total, '1')
        return verificado

    def segundo_verificador():
        total = 0
        multiplicador = 11
        for i in range(10):
            total += int(cpf[i]) * multiplicador
            multiplicador -= 1

        verificado = calcular_digito_verificador(total, '2')
        return verificado

    primeiro = primeiro_verificador()
    segundo = segundo_verificador()


    if primeiro == 1 and segundo == 1:
        return 1
    else:
        return 0


if __name__ == '__main__':
    validacao_cpf('012.303.399-30')