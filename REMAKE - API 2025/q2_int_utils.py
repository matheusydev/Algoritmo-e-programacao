def obter_numero_inteiro(label: str):
    entrada = input(label)
    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print(f'O que você colocou "{entrada}" não é um número inteiro')
        print("Tente novamente! ")
        return obter_numero_inteiro(label)


def obter_numero_inteiro_positivo(label: str):
    entrada = input(label)
    try:
        numero = int(entrada)
        if numero > 0:
            return numero
        else:
            print(f'O número "{entrada}" não é positivo(maior que 0)')
            print("Tente novamente! ")
            return obter_numero_inteiro_positivo(label)
    except ValueError:
        print(f'O que você colocou "{entrada}" não é um número inteiro')
        print("Tente novamente! ")
        return obter_numero_inteiro_positivo(label)


def obter_numero_inteiro_minimo(label: str):
    min = int(input("Insira o valor mínimo: "))
    entrada = input(label)
    try:
        numero = int(entrada)
        if numero > min:
            return numero
        else:
            print(f'O número "{entrada}" não é maior que {min}')
            print("Tente novamente! ")
            return obter_numero_inteiro_minimo(label)
    except ValueError:
        print(f'O que você colocou "{entrada}" não é um número inteiro válido')
        print("Tente novamente! ")
        return obter_numero_inteiro_minimo(label)
    

def obter_numero_inteiro_maximo(label: str):
    max = int(input("Insira o valor máximo: "))
    entrada = input(label)
    try:
        numero = int(entrada)
        if numero < max:
            return numero
        else:
            print(f'O número "{entrada}" deve ser menor que {max}')
            print("Tente novamente! ")
            return obter_numero_inteiro_maximo(label)
    except ValueError:
        print(f'O que você colocou "{entrada}" não é um número inteiro válido')
        print("Tente novamente! ")
        return obter_numero_inteiro(label)
    

def obter_numero_inteiro_faixa(label: str):
    min = int(input("Insira o valor mínimo: "))
    max = int(input("Insira o valor máximo: "))
    entrada = input(label)
    try:
        numero = int(entrada)
        if min < numero < max:
            return numero
        else:
            print(f'O número "{entrada}" deve está entre {min} a {max}')
            print("Tente novamente! ")
            return obter_numero_inteiro_faixa(label)
    except ValueError:
        print(f'O que você colocou "{entrada}" não é um número inteiro válido')
        print("Tente novamente! ")
        return obter_numero_inteiro_faixa(label)