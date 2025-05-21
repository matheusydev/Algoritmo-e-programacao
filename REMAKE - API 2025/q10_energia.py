import utils
def main():

    consulta = utils.obter_numero_inteiro("Insira a quantidade de consulta: ") 
    contador = 0
    nome = None
    kwh = 0
    bandeira = 0

    while contador < consulta:
        nome = utils.obter_string("Qual o nome do consumidor: ")
        kwh = utils.obter_numero_inteiro("Quanto foi o consumo em KWh: ")
        bandeira = utils.obter_numero_real("Insira um a taxa da bandeira em porcentagem(%): ")

        if kwh < 30:
            print(insento)
            contador += 1


    insento = (f"""****** TALÃO MENSAL XPTO ******
Consumidor: {nome} 
Consumo (KWh): {kwh}
---------------------------------------------
Total a Pagar: R$: 0,00
""")

main()