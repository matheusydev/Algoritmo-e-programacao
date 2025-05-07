from functions import obter_numero_inteiro

def main():

    lado1 = obter_numero_inteiro("Insira o valor do primeiro lado: ")
    lado2 = obter_numero_inteiro("Insira o valor do segundo lado: ")
    lado3 = obter_numero_inteiro("Insira o valor do terceiro lado: ")


    if lado1 == 0 or lado2 == 0 or lado3 == 0:
        print("Lados inválidos: não pode ser 0 ")
    elif (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        if lado1 == lado2 == lado3:
            print("Triângulo Equilátero")
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("Triângulo Isósceles")
        else:
            print("Triângulo Escaleno")
    else:
        print("Os lados fornecidos NÃO formam um triângulo.")

main()