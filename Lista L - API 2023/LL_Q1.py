import utils
def main():

    num_compras = utils.obter_numero_interio("Quantas compras vocês fez no mês: ")
    cliente = str(input("Digite o seu nome: "))


    contador = 0
    cashbacktotal = 0
    cashback_maior = None
    soma_compras = 0
    cashback_menor = None

    while num_compras > contador: 
        
        preco = utils.obter_numero_interio("Entre com o preço da compra")
        cashbacktotal += cashback
        soma_compras += preco


        catador += 1

        if cashback_maior == None or cashback_maior > cashback(preco):
            cashback_maior = cashback(preco)
        if cashback_menor == None or cashback_menor < cashback_menor:
            cashback_menor = cashback(preco)

        media_cashback = media(cashbacktotal,num_compras)
        percentual = cashbacktotal / soma_compras

    interface = f'''=== LOJAS MATSKI ===
> CLIENTE: {cliente}
> TOTAL EM COMPRAS: R${soma_compras:.2f}
> TOTAL EM CASHBACK: R${cashbacktotal:.2f}
> PERCENTUAL INVESTIDO EM CASHBACK PELA LOJA: {percentual:.2f}%
> MAIOR VALOR DE CASHBACK: R${cashback_maior:.2f}
> MENOR VALOR DE CASHBACK: R${cashback_menor:.2f}
> VALOR MÉDIO DE CASHBACK: R${media_cashback:.2f}
'''
    print(interface)


def cashback(preco):
    if preco <= 250:
        return preco * 0.05
    elif preco <= 500:
        return preco * 0.07
    elif preco <= 750:
        return preco * 0.08
    else:
        return (250 * 0.05) + (500 * 0.07) + (750 * 0.08) + (preco - 750) * 0.25

def media(soma: float, n: int):
    return soma/n

main()
