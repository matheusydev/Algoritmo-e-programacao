from io_utils import obter_numero_inteiro

def main():

    numero = obter_numero_inteiro('Insira um número: ')

    resultado = verifica_se_eh_primo(numero)

    print(f'o número {numero} {resultado}')

def verifica_se_eh_primo(numero):
    if numero % 2 == 0:
        return 'não é primo'
    elif numero % 3 == 0:
        return 'não é primo'
    elif numero % 5 == 0:
        return 'não é primo'
    elif numero % 7 == 0:
        return 'não é primo'    
    elif numero % 11 == 0:
        return 'não é primo'
    else:
        return 'é primo'


    




main()