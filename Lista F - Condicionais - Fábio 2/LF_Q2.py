from functions import obter_numero_inteiro

def main():
    numero1 = obter_numero_inteiro("Insira o primeiro número: ")
    numero2 = obter_numero_inteiro("Insira o segundo número: ")

    resultado = verifica_maior_e_menor(numero1, numero2)

def verifica_maior_e_menor(numero1, numero2):
    if numero1 > numero2:
        return print(f'o maior número é o {numero1}')
    elif numero2 > numero1:
        return print(f'o maior número é o {numero2}')
    else:
        return print('os dois números são iguals')

main()