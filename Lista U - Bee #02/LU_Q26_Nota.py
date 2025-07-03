def main():
    soma = 0
    x = 2
    while x != 0:
        nota = float(input())

        if nota > 0 and nota < 11:
            soma += nota
            x -= 1
        else:
            print("nota invalida")

    media = soma / 2

    print(f"media = {media:.2f}")
main()