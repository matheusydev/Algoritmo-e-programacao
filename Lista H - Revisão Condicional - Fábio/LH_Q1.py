import utils

def main(): 

    utils.clear()
    numero = utils.obter_numero_real("Insira um número: ")
    utils.clear()

    if numero > 0:
        print("Seu número é positivo :)")
    else:
        print("Seu número é negativo :(")

    print("FIM")


main()