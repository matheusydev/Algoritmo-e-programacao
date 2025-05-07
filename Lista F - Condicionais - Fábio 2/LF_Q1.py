from functions import obter_numero_inteiro

def main():
    numero1 = obter_numero_inteiro("Insira o primeiro número: ")
    numero2 = obter_numero_inteiro("Insira o segundo número: ")
    numero3 = obter_numero_inteiro("Insira o terceiro número: ")

    iguais1_2 = obter_numeros_iguais_1_2(numero1, numero2)
    iguais2_3 = obter_numeros_iguais_2_3(numero2, numero3)
    iguais1_3 = obter_numeros_iguais_1_3(numero1, numero3)

    print(f'entre {numero1} e {numero2} temos {iguais1_2} números iguais')
    print(f'entre {numero2} e {numero3} temos {iguais2_3} números iguais')
    print(f'entre {numero1} e {numero3} temos {iguais1_3} números iguais')

def obter_numeros_iguais_1_2(numero1: int, numero2: int):
    return (numero2 - numero1) - 1


def obter_numeros_iguais_2_3(numero2: int, numero3: int):
    return (numero3 - numero2) - 1


def obter_numeros_iguais_1_3(numero1: int, numero3: int):
    return (numero3 - numero1) - 1
    

main()

