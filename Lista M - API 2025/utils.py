import os

def obter_numero_inteiro(label: str):
    entrada = input(label)
    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print(f'O que você colocou "{entrada}" não é um número inteiro')
        return obter_numero_inteiro(label)



def obter_numero_real(label: str):
    entrada = input(label)
    try:
        numero = float(entrada)
        return numero
    except ValueError:
        print(f'O que você colocou "{entrada}" não é um número real')
        return obter_numero_real(label)
    
def clear():
    os.system('cls')

def enter_continue():
    input("Enter para continuar")


def linha():
    print("=" * 30)

def obter_string(label: str):
    return input(label)
