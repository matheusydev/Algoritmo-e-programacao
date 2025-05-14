import utils

def main(): 

    utils.clear()
    sexo = utils.obter_string("Entre com M ou F: ")
    utils.clear()

    if sexo == "M":
        print("sexo masculino")
    elif sexo == "F":
        print("sexo feminino")
    else:
        print("sexo invalido")

    print("FIM")


main()