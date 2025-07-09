# a. Pedir um Número
def obter_numero_inteiro(label):
    entrada = input
    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print(f'A entrada "{entrada}" não é um número inteiro.')
        print("Tente novamente!")
        return obter_numero_inteiro(label)
    
# b. Pedir um Número Positivo
def obter_numero_inteiro_positivo(label):
    entrada = input
    try:
        numero = int(entrada)
        if numero > 0:
            return numero
        else:
            print(f"A entrada {entrada} não é um número positivo")
            print("Tente novamente!")
            return obter_numero_inteiro_positivo(label)
    except ValueError:
        print(f'A entrada "{entrada}" não é um número inteiro.')
        print("Tente novamente!")
        return obter_numero_inteiro_positivo(label)
    
# c. Pedir um Número Negativo
def obter_numero_inteiro_negativo(label):
    entrada = input
    try:
        numero = int(entrada)
        if numero < 0:
            return numero
        else:
            print(f"A entrada {entrada} não é um número negativo")
            print("Tente novamente!")
            return obter_numero_inteiro_negativo(label)
    except ValueError:
        print(f'A entrada "{entrada}" não é um número inteiro.')
        print("Tente novamente!")
        return obter_numero_inteiro_negativo(label)
    
# d. Pedir um Número da Faixa
def obter_numero_inteiro_faixa(label: str, min: int, max: int):
    entrada = input(label)
    try:
        numero = int(entrada)
        if min < numero < max:
            return numero
        else:
            print(f'O número "{entrada}" deve está entre {min} a {max}')
            print("Tente novamente! ")
            return obter_numero_inteiro_faixa(label, min, max)
    except ValueError:
        print(f'O que você colocou "{entrada}" não é um número inteiro válido')
        print("Tente novamente! ")
        return obter_numero_inteiro_faixa(label, min, max)
    
# e. Pedir um Número inteiro
def obter_numero_real(label):
    entrada = input
    try:
        numero = float(entrada)
        return numero
    except ValueError:
        print(f'A entrada "{entrada}" não é um número inteiro.')
        print("Tente novamente!")
        return obter_numero_real(label)

# d. Pedir um Número da Faixa