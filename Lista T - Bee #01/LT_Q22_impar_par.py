def main():
    positivo = 0
    negativo = 0
    par = 0
    impar = 0

    for _ in range(5):
        num = float(input())
        if num % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
        if num > 0:
            positivo = positivo + 1
        elif num < 0:
            negativo = negativo + 1

    print(f"{par} valor(es) par(es)")
    print(f"{impar} valor(es) impar(es)")
    print(f"{positivo} valor(es) positivo(s)")
    print(f"{negativo} valor(es) negativo(s)")
main()