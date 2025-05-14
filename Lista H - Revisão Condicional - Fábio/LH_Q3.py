import utils

def main(): 

    utils.clear()
    letra = utils.obter_string("Entre com uma letra: ")
    utils.clear()

    if letra.upper() == "A":
        print("vogal")
    elif letra.upper() == "E":
        print("vogal")
    elif letra.upper() == "I":
        print("vogal")
    elif letra.upper() == "O":
        print("vogal")
    elif letra.upper() == "U":
        print("vogal")
    else:
        print("consoante")

    print("FIM")


main()