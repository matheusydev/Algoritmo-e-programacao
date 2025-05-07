from io_utils import obter_numero_real, obter_string

def main():

    compra = obter_numero_real('Insira o valor da compra: ')
    vip = obter_string('Você é um cliente VIP? ') 
    aniversario = obter_string('Hoje é seu Aniversário? ')

    descontovip = eh_vip(vip)
    descontoaniversario = eh_aniversariante(aniversario)
    descontocompra = desconto_sobre_valor(compra)

    valorfinal = calcular_desconto(compra, descontovip, descontoaniversario, descontocompra)

    print(f'a compra de R$:{compra:.2f} fica por R$:{valorfinal:.2f}')

def eh_vip(vip):
    if vip == "sim":
        return 0.95
    elif vip == "não":
        return 1
    else:
        print('Resposta inválida. Responda com "sim" ou "não".')
        vip_resposta = obter_string('Você é um cliente VIP? ')
        return eh_vip(vip_resposta)
    

def eh_aniversariante(aniversario):
    if aniversario == "sim":
        return 0.97
    elif aniversario == "não":
        return 1
    else:
        print('Resposta inválida. Responda com "sim" ou "não".')
        aniversario_resposta = obter_string('Hoje é seu Aniversário? ')
        return eh_vip(aniversario_resposta)


def desconto_sobre_valor(compra: float):
    if compra > 500:
        return 0.85
    elif compra > 200:
        return 0.9
    elif compra > 100:
        return 0.95
    else:
        return 1 


def calcular_desconto(compra, descontovip, descontoaniversario, descontocompra):
    return compra * descontovip * descontoaniversario * descontocompra




main()