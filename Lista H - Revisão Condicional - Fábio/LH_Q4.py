import utils

def main(): 

    utils.clear()
    nota1 = utils.obter_numero_real("Insira a primeira nota: ")
    nota2 = utils.obter_numero_real("Insira a segunda nota: ")
    utils.clear()

    media = (nota1 + nota2 ) / 2

    if media == 10:
        print("Aprovado com distinção")
    elif media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

    print("FIM")


main()