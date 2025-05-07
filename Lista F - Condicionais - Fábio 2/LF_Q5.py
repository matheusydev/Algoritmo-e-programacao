from functions import obter_numero_inteiro

def main():
    numero1 = obter_numero_inteiro("Insira o primeiro número: ")
    numero2 = obter_numero_inteiro("Insira o segundo número: ")
    numero3 = obter_numero_inteiro("Insira o terceiro número: ")

    resultado = verifica_a_ordem(numero1, numero2, numero3)

def verifica_a_ordem(numero1: int, numero2: int, numero3: int):
    if numero1 > numero2 and numero1 > numero3 and numero2 > numero3:
        return print(f'{numero3}, {numero2}, {numero1}')
    elif numero1 > numero2 and numero1 > numero3 and numero3 > numero2:
        return print(f'{numero2}, {numero3}, {numero1}')
    elif numero2 > numero1 and numero2 > numero3 and numero2 > numero1:
        return print(f'{numero3}, {numero1}, {numero2}')

    elif numero3 > numero1 and numero3 > numero2 and numero2 > numero1:
        return print(f'{numero1}, {numero2}, {numero3}')
    else:
        return print(f'{numero2}, {numero1}, {numero3}')


main()