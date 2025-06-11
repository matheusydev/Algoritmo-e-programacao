def main():
    imoveis = int(input('Insira o número de imóveis: '))
    maior_retorno = None
    maior_taxa = None
    inde_imov = None
    

    for _ in range(1, imoveis+1):
        print(f'Imóvel nº: {_}')
        indentificador = int(input("Insira o código indentificador do imóvel"))
        valor_compra = int(input('Insira o valor de compra do imóvel: '))
        valor_aluguel = int(input('Insira o valor mensal do aluguel: '))
        anos_alugado = int(input('Insira quantos anos o imóvel ficou alugado em anos: '))

        retorno_total = ((valor_aluguel*12)*anos_alugado) - valor_compra

        taxa_retorno = retorno_total/ anos_alugado
        retorno_anual = (taxa_retorno*100)/valor_compra

        if maior_taxa == None or retorno_anual > maior_taxa:
            maior_taxa = retorno_anual

        if maior_retorno == None or retorno_total > maior_retorno:
            maior_retorno = retorno_total
            inde_imov = indentificador


    print(f'''============== RESULTADO ==============
Retorno total: R${retorno_total:.2f}
Taxa de retorno anualizada: {retorno_anual:.2f}%
Código do imóvel com maior retorno: {inde_imov}
Maior retorno: R${maior_retorno:.2f}
Maior taxa: {maior_taxa:.2f}%
''')


main()

