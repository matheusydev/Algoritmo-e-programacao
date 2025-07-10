import os
import time
import sys

# a. Pedir um Número
def obter_numero_inteiro(label):
    entrada = input(label)
    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print(f'A entrada "{entrada}" não é um número inteiro.')
        print("Tente novamente!")
        return obter_numero_inteiro(label)
    
# b. Pedir um Número Positivo
def obter_numero_inteiro_positivo(label):
    entrada = input(label)
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
    entrada = input(label)
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
def obter_numero_inteiro_faixa(label, minimo, maximo):
    entrada = input(label)
    try:
        numero = int(entrada)
        if minimo <= numero <= maximo:
            return numero
        else:
            print(f'O número "{entrada}" deve está entre {minimo} a {maximo}')
            print("Tente novamente! ")
            return obter_numero_inteiro_faixa(label, minimo, maximo)
    except ValueError:
        print(f'O que você colocou "{entrada}" não é um número inteiro válido')
        print("Tente novamente! ")
        return obter_numero_inteiro_faixa(label, minimo, maximo)
    
# e. Pedir um Número inteiro
def obter_numero_real(label):
    entrada = input(label)
    try:
        numero = float(entrada)
        return numero
    except ValueError:
        print(f'A entrada "{entrada}" não é um número inteiro.')
        print("Tente novamente!")
        return obter_numero_real(label)

def inicializar():
    
    os.system('cls')
    print(">>>>>>>>>> PlayNumbers <<<<<<<<<<")
    time.sleep(0.8)

    print("Deseja carregar o programa?")
    time.sleep(0.8)

    enter_to_continue()

    print("Carregando programa")
    time.sleep(0.8)  
    os.system('cls')

    start_time = time.time()
    while time.time() - start_time < 3:  
        print(".", end="")
        sys.stdout.flush()  
        time.sleep(0.1)
    time.sleep(0.8)  
    os.system('cls')

#Enter to continue
def enter_to_continue():
    time.sleep(0.8)
    input(f"\nPrecione enter para continuar ")
    time.sleep(0.8)
    os.system('cls')

#clear
def clear():
    os.system('cls')