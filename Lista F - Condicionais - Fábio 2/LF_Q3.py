from functions import obter_numero_inteiro

def main():
    numero1 = obter_numero_inteiro("Insira o primeiro número: ")
    numero2 = obter_numero_inteiro("Insira o segundo número: ")
    numero3 = obter_numero_inteiro("Insira o terceiro número: ")

    maior = numero1

    if numero2 > maior:
        maior = numero2

    if numero3 > maior:
        maior = numero3


    print(f"O numero maior é o {maior}")

main()
