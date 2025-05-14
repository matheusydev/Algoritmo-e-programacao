import utils

def main(): 

    utils.clear()
    turno = utils.obter_string("Entre com M, V, N: ")
    utils.clear()

    if turno.upper() == "M":
        print("Bom dia!")
    elif turno.upper() == "V":
        print("Boa tarde!")
    elif turno.upper() == "N":
        print("Boa noite!")
    else:
        print("valor inválido")

    print("FIM")


main()