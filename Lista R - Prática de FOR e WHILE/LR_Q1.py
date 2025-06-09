def main():
    ...
    dias = int(input('Dias: '))
    limite_cal = int(input('Limite calórico: '))


    soma_calorias = 0
    calorias_por_dia = 0
    dia_mais_calorico = None
    dia_menos_calorico = None
    for dia in range(1, dias+1, 1):
        print(f'Dia: {dia}')
        cafe = int(input('Café: '))
        almoco = int(input('Almoço: '))
        lanche = int(input('Lanche: '))
        janta = int(input('Janta: '))

        calorias_por_dia = cafe + almoco + lanche + janta
        soma_calorias += calorias_por_dia
        if dia_mais_calorico == None or calorias_por_dia > dia_mais_calorico:
            dia_mais_calorico = dia
        if dia_menos_calorico == None or calorias_por_dia < dia_menos_calorico:
            dia_menos_calorico = dia

    media_diaria_calorica = calcular_media(soma_calorias, dias)
    print(f'''=== ANÁLISE HENRIQUE JAMBO CALORIAS ===
MÉDIA CALÓRICA DIÁRIA DO PERÍODO: {media_diaria_calorica:.1f} CALORIAS
DIA DE MENOR CONSUMO: DIA {dia_menos_calorico}
DIA DE MAIOR CONSUMO: DIA {dia_mais_calorico}
{comparar_media_diaria(limite_cal, media_diaria_calorica)}
    ''')

def maior_consumo(calorias_por_dia: int, dia: int, dia_mais_calorico: int ):
    if dia_mais_calorico == None or calorias_por_dia > dia_mais_calorico:
        dia_mais_calorico = dia

def menor_consumo(calorias_por_dia: int, dia: int, dia_menos_calorico: int):
    if dia_menos_calorico == None or calorias_por_dia < dia_menos_calorico:
        dia_menos_calorico = dia

def comparar_media_diaria(limite_cal: int, media_diaria_calorica: int):
    if limite_cal < media_diaria_calorica: 
        return 'Você excedeu o limite diário de calorias (SEU IMENSOOOOOOOOOOOOOOOOOOOOOO)'
    else: 
        return 'Você NÃO excedeu o limite diário de calorias (SEU PATROCINIOOOOOOOOO)'
        
def calcular_media(soma, n):
    return soma/n



main()