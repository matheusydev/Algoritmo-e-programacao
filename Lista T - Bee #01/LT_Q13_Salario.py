def main():

    entrada = float(input())

    if entrada <= 400:
        porcentagem = 15
        reajuste = entrada * (15/100)
        salario = entrada + reajuste
    elif entrada <= 800:
        porcentagem = 12
        reajuste = entrada * (12/100)
        salario = entrada + reajuste
    elif entrada <= 1200:
        porcentagem = 10
        reajuste = entrada * (10/100)
        salario = entrada + reajuste
    elif entrada <= 2000:
        porcentagem = 7
        reajuste = entrada * (7/100)
        salario = entrada + reajuste
    else:
        porcentagem = 4
        reajuste = entrada * (4/100)
        salario = entrada + reajuste

    print(f'Novo salario: {salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: {porcentagem} %')


main()