from functions import obter_numero_inteiro

def main():

    numero = obter_numero_inteiro("Insira um número entre 0 á 100(não pode ser 1): ")
    numero = verifica_o_numero(numero)

    resultado = verifica_se_eh_primo(numero)
    print(f'O número {numero} {resultado}')


def verifica_o_numero(numero: int):
    if numero <= 0 or numero > 100 or numero == 1:
        print('Resposta inválida. O número tem que estar entre 0 e 100 e não pode ser 1.')
        novonumero = obter_numero_inteiro("Insira novamente um número: ")
        return verifica_o_numero(novonumero)
    else:
        return numero

    
def verifica_se_eh_primo(numero: int):
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