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
    

def obter_string(label: str):
    return input(label)
    
def obter_numero_real_q3(label: str):
    min_valor = 0
    max_valor = 10
    entrada = input(label)
    try:
        numero = float(entrada)
        if min_valor <= numero <= max_valor:
            return numero
        else:
            print(f"A nota deve estar entre {min_valor} e {max_valor}.")
            return obter_numero_real(label)
    except ValueError:
        print(f'O que você colocou "{entrada}" não é um número real.')
        return obter_numero_real(label)


def show_menu_5():
    menu = """
    ======= MENU PRINCIPAL =======
    1 - Descrição
    2 - Especificação 
    3 - Valor
    0 - Sair
    """
    print(menu)
    
def linha():
    linha = "-" * 30
    print(linha) 


def clear():
    os.system('cls')


