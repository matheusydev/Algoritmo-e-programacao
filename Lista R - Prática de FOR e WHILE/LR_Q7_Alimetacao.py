def main():

    itens = []
    qtd_itens = int(input("Insira a quantidade de itens: "))

    for item in range(1, qtd_itens + 1):
        nome = str(input(f'Insira o nome do produto{item}: '))
        quantidade = int(input('Insira a quantidade: '))
        dia_compra, mes_compra, ano_compra = map(int,input('Insira a data de compra(DD/MM/AAAA): ').split('/')) 
        dia_vencimento, mes_vencimento, ano_vencimento = map(int,input('Insira a data de validade(DD/MM/AAAA): ').split('/')) 

        total_compra = dia_compra + (mes_compra * 30) + (ano_compra * 360)
        total_vencimento = dia_vencimento + (mes_vencimento * 30) + (ano_vencimento * 360)

        if total_compra > total_vencimento:
            dias_restante = "Vencido"
        else:
            dias_restante = f"{total_vencimento - total_compra} dias restantes"

        data = f"{dia_vencimento:02d}/{mes_vencimento:02d}/{ano_vencimento}"

        itens.append({
            "nome":nome, 
            "quantidade": quantidade, 
            "validade": dias_restante,
            "data": data
        })


        # dia_restante = (dia_compra - dia_vencimento) + ((mes_compra * 30) - (mes_vencimento * 30)) + ((ano_compra * 360) - (ano_vencimento * 360))
        # print(dia_restante)

    print(itens)
        
        






main()