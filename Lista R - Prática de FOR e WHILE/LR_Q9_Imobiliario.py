def main():
    imovel = float(input("Insira o valor do imóvel em (R$): "))
    entrada = float(input("Insira o valor da entrada em (R$): "))
    taxa_juros = float(input("Insira a taxa(%): ")) / 100
    qtd_parcelas = int(input("Insira a quantidade de parcelas: "))
    saldo_devedor = imovel - entrada
    valor_parcela = (saldo_devedor * taxa_juros) / (1 - (1 + taxa_juros)**(qtd_parcelas * (-1)))
    juros = 0
    amortizacao = 0

    for _ in range(1, qtd_parcelas + 1):
        juros = saldo_devedor * taxa_juros
        amortizacao = valor_parcela - juros
        atual = saldo_devedor - amortizacao
        saldo_devedor = atual
        
        print(f'''================= BOLETO GERADO {_}° PARCELA =================
Valor da parcela: R$: {valor_parcela:.2f}
Valor do juros da parcela: R$: {juros:.2f}
Saldo devedor da parceala: R${atual:.2f}
        ''')

    print(f"""
PROGRAMA FINALIZADO
""")


main()