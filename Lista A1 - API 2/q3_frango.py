import utils
def main():

    maximo_caixas = utils.obter_numero_inteiro_positivo("Insira a quantidade de caixas: ")
    maximo_peso_ton = utils.obter_numero_real("Insira o peso em toneladas: ")

    maximo_peso_kg = maximo_peso_ton * 1000

    somatorio_peso = 0
    peso_caixa = 1

    while peso_caixa != 0 and somatorio_caixas < maximo_caixas and somatorio_peso < maximo_peso_kg:
        peso_caixa = utils.obter_numero_real("Insira o peso da caixa em kg (ou 0 para encerrar): ")

        somatorio_peso += peso_caixa
        somatorio_caixas += 1


    print(f"Total de caixas carregadas: {somatorio_caixas}")
    print(f"Peso total da carga: {somatorio_peso:.2f} kg")

main()