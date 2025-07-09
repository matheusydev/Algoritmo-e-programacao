def main():
    N = int(input())

    pontos_por_dimensao = (2 ** N) + 1

    total_pontos = pontos_por_dimensao * pontos_por_dimensao

    print(total_pontos)
main()