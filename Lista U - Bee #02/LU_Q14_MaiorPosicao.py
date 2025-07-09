def main():
    maior = 0
    posicao = 0

    for i in range(1, 101):
        num = int(input())
        if num > maior:
            maior = num
            posicao = i

    print(maior)
    print(posicao)

main()