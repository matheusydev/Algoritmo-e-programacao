#oi Malu. Tudo bom?
alimentos = {
    'amendoim_japones': {'calorias': 500, 'proteinas': 14},
    'banana_nanica': {'calorias': 89, 'proteinas': 1.1},
    'frango_grelhado': {'calorias': 165, 'proteinas': 31},
    'arroz_integral': {'calorias': 111, 'proteinas': 2.6},
    'feijao_preto': {'calorias': 132, 'proteinas': 8.9},
    'ovo_cozido': {'calorias': 77, 'proteinas': 6.3},
    'abacate': {'calorias': 160, 'proteinas': 2},
    'batata_doce': {'calorias': 86, 'proteinas': 1.6},
    'salmão_grelhado': {'calorias': 208, 'proteinas': 20},
    'iogurte_natural': {'calorias': 61, 'proteinas': 3.5}
}

def main():
    pessoas = int(input('Insira a quantidade de pessoas: '))
    maior_consumo = None
    menor_consumo = None
    for pessoa in range(1, pessoas + 1, 1):
        print(f'Pessoa {pessoa}')
        qtd_produto = int(input('Qtd de produtos: '))

        for produto in range(1, qtd_produto+1):
            nome = obter_alimento()
            gramas = float(input('Peso (g): '))


            calorias = (alimentos[nome]['calorias'] * gramas) / 100
            proteinas =  (alimentos[nome]['proteinas'] * gramas) / 100

            total_calorias += calorias
            total_proteinas += proteinas
        print(f'Consumo calórico: {total_calorias} calorias\nConsumo proteico: {total_proteinas}g de proteína')

        if maior_consumo == None or total_calorias > maior_consumo:
            maior_consumo = total_calorias
        if menor_consumo == None or total_calorias < menor_consumo:
            menor_consumo = total_calorias
    print(f'Maior consumo calórico: {maior_consumo}\nMenor consumo: {menor_consumo}')


            

def obter_alimento():
    while True:
        nome = str(input('Insira o produto: ')).lower()
        if nome in alimentos:
            return nome
        else:
            print('Alimento Inválido. Tente novamente')
            obter_alimento()
main()