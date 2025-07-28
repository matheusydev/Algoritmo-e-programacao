import utils
def main():
    qtd_bombas = utils.obter_numero_inteiro_positivo("Insira a quantidade de bombas: ")
    valor_inicial = utils.obter_numero_real_positivo("Insira o valor inicial de barris por bomba: ")
    reducao_percentual = utils.obter_numero_faixa_float("Insira o valor de redução por ciclo (%): ", 0, 100) / 100
    limite_minimo = utils.obter_numero_real_positivo("Insira o limite mínimo de barris por bomba: ")
    
    ciclos = 1
    total_barris = valor_inicial * qtd_bombas

    valor_atual = valor_inicial

    while valor_atual > limite_minimo:
        valor_atual *= (1 - reducao_percentual)
        total_barris += valor_atual * qtd_bombas
        ciclos += 1

    print(f"Será possível realizar {ciclos} ciclos")
    print(f"A quantidade de barris retirados é de {total_barris:.2f} barris")

main()
