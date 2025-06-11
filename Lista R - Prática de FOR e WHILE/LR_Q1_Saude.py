def main():
    dias = int(input('Dias: '))
    limite_cal = int(input('Limite calórico: '))

    soma_calorias = 0
    dia_mais_calorico = None
    dia_menos_calorico = None

    for dia in range(1, dias+1):
        print(f'Dia: {dia}')
        cafe = int(input('Café: '))
        almoco = int(input('Almoço: '))
        lanche = int(input('Lanche: '))
        janta = int(input('Janta: '))

        calorias_do_dia = cafe + almoco + lanche + janta
        soma_calorias += calorias_do_dia

        dia_mais_calorico = maior_consumo(calorias_do_dia, dia, dia_mais_calorico)
        dia_menos_calorico = menor_consumo(calorias_do_dia, dia, dia_menos_calorico)
        print(f"mais: {dia_mais_calorico}, menos: {dia_menos_calorico}")

    media_diaria_calorica = calcular_media(soma_calorias, dias)

    print(f'''=== ANÁLISE HENRIQUE JAMBO CALORIAS ===
MÉDIA CALÓRICA DIÁRIA DO PERÍODO: {media_diaria_calorica:.1f} CALORIAS
DIA DE MENOR CONSUMO: DIA {dia_menos_calorico[1]}
DIA DE MAIOR CONSUMO: DIA {dia_mais_calorico[1]}
{comparar_media_diaria(limite_cal, media_diaria_calorica)}
    ''')

def maior_consumo(calorias_por_dia, dia, dia_mais_calorico):
    if dia_mais_calorico is None or calorias_por_dia > dia_mais_calorico[0]:
        return (calorias_por_dia, dia)
    return dia_mais_calorico

def menor_consumo(calorias_por_dia, dia, dia_menos_calorico):
    if dia_menos_calorico is None or calorias_por_dia < dia_menos_calorico[0]:
        return (calorias_por_dia, dia)
    return dia_menos_calorico

def comparar_media_diaria(limite_cal, media_diaria_calorica):
    if limite_cal < media_diaria_calorica: 
        return 'Você excedeu o limite diário de calorias'
    else: 
        return 'Você NÃO excedeu o limite diário de calorias'
        
def calcular_media(soma, n):
    return soma/n

main()
