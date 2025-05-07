from functions import obter_numero_inteiro

def main():

    numero = obter_numero_inteiro("Insira o número: ")


    dezena = numero // 10
    unidade = numero % 10

    if dezena == unidade:
        print(f"Os algarismos da dezena e da unidade são iguais ({dezena} = {unidade})")
    else:
        print(f"Os algarismos da dezena e da unidade são divergente ({dezena} e {unidade})")

main()
