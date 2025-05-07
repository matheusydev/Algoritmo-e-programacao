from functions import obter_numero_inteiro

def main():

    angulo1 = obter_numero_inteiro("Insira o primeiro ângulo: ")
    angulo2 = obter_numero_inteiro("Insira o segundo ângulo: ")
    angulo3 = obter_numero_inteiro("Insira o terceiro ângulo: ")

    if angulo1 == 0 or angulo2 == 0 or angulo3 == 0:
        print("Ângulos inválidos: não pode ser 0")
    elif angulo1 + angulo2 + angulo3 != 180:
        print("Não formam um triângulo: a soma dos ângulos deve ser 180º.")
    else:
        if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
            print("triângulo acutângulo")
        elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
            print("triângulo retângulo")
        else:
            print("triângulo obtusângulo")

main()