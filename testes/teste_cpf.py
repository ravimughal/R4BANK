import random

def gerar_cpf():
    cpf = [str(random.randint(0, 9)) for _ in range(9)]
    
    # Cálculo do dígito verificador 1
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    cpf.append(str(11 - resto) if resto > 1 else '0')
    
    # Cálculo do dígito verificador 2
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    cpf.append(str(11 - resto) if resto > 1 else '0')
    
    return ''.join(cpf)


