import utils
def main(): 

    largura = utils.obter_numero_real("Entre com o valor da largura da piscina: ")
    altura  = utils.obter_numero_real("Entre com o valor da altura da piscina: ")
    profundidade = utils.obter_numero_real("Entre com o valor da profundidade da piscina: ")
    preco_do_litro = utils.obter_numero_real("Entre com o preço do litro: ")


    volume = (largura * altura * profundidade) / 1000
    volume_ideal = volume * 0.85
    valor_encher = (volume_ideal / 1000) * preco_do_litro
    valor_mensal = valor_encher * 0.1

    print(f"""========================= Festa na piscina do Matheus =========================
      
VOLUME DA PISCINA = {volume}
VOLUME IDEAL = {volume_ideal}
VALOR DE ENCHER A PISCINA = {valor_encher}
VALOR MENSAL = {valor_mensal}
      
""")

main()