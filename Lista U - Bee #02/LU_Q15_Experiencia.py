def main():
    N = int(input())

    coelho = 0
    rato = 0
    sapo = 0
    soma = 0
    for i in range(N):
        entrada = input().split()
        qtd = int(entrada[0])
        animal = entrada[1]

        soma += qtd

        if animal == 'C':
            coelho += qtd
        elif animal =='R':
            rato += qtd
        elif animal =='S':
            sapo += qtd

    print(f"Total: {soma} cobaias")
    print(f"Total de coelhos: {coelho}")
    print(f"Total de ratos: {rato}")
    print(f"Total de sapos: {sapo}")
    print(f"Percentual de coelhos: {((100*coelho)/soma):.2f} %")
    print(f"Percentual de ratos: {((100*rato)/soma):.2f} %")
    print(f"Percentual de sapos: {((100*sapo)/soma):.2f} %")

main()