from functions import obter_numero_inteiro

def main():
    numero = obter_numero_inteiro("Insira um número: ")

    resultado = verifica_par_ou_impar(numero)

def verifica_par_ou_impar(numero):
    if numero % 2 == 0:
        return print(f'o número {numero} é par')
    else:
        return print(f'o número {numero} é ímpar')

main()