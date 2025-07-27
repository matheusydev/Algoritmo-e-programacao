import utils

def main():
    qtd_provas = utils.obter_numero_faixa("Insira a quantidade de provas (2 a 6): ", 2, 6)
    somatorio = 0
    somatorio_ponderado = 0
    somatorio_peso = 0

    for i in range(1, qtd_provas + 1):
        nota = utils.obter_numero_faixa(f"Insira a nota {i} (0 a 10): ", 0, 10)
        peso = utils.obter_numero_faixa(f"Insira o peso da prova {i} (1 a 3): ", 1, 3)

        somatorio += nota
        somatorio_ponderado += nota * peso
        somatorio_peso += peso

    media_sistema_comum = somatorio / qtd_provas
    media_ponderada = somatorio_ponderado / somatorio_peso

    if media_ponderada >= 8.0:
        print(f"PARABÉNS! Sua média ponderada é {media_ponderada:.1f}. Você passou!!!")
    else:
        print(f"Infelizmente você não passou. Sua média ponderada foi {media_ponderada:.1f}, inferior a 8.0.")

    print(f"Sua média no sistema comum: {media_sistema_comum:.1f}")

main()
