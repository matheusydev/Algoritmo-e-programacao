#FEITO POR MALU & MATHEUS
def main():
    
    qtd_anos = int(input('Insira a quantidade de anos: '))
    temp_acumulada = 0
    temp_min = None
    ano_min = None
    temp_max = None
    ano_max = None
    first_half = (qtd_anos // 2)
    temp_first = 0
    temp_second = 0
    ano = 1

    for ano in range(1, first_half + 1):
        temperatura = float(input(f'Insira a tempretatura do ano {ano}: '))
        
        temp_acumulada += temperatura
        temp_first += temperatura
        
        if temp_min == None or temperatura < temp_min:
            temp_min = temperatura
            ano_min = ano
        print(f'{temp_min} {ano_min} {temp_first} {temp_second}')
            
        if temp_max == None or temperatura > temp_max:
            temp_max = temperatura
            ano_max = ano
        print(f'{temp_max} {ano_max}')

    for ano in range(first_half + 1, qtd_anos + 1):
        temperatura = float(input(f'Insira a tempretatura do ano {ano}: '))
        
        temp_acumulada += temperatura
        temp_second += temperatura
        
        if temp_min == None or temperatura < temp_min:
            temp_min = temperatura
            ano_min = ano
        print(f'{temp_min} {ano_min}')
            
        if temp_max == None or temperatura > temp_max:
            temp_max = temperatura
            ano_max = ano
        print(f'{temp_max} {ano_max}')
    
    media = temp_acumulada / qtd_anos
    estado = verifica_estado(temp_first, temp_second)
    
    resultado = f'''
    TOTAL DE ANOS: {qtd_anos}
    MÉDIA DE TEMPERATURA: {media}
    ANO DA TEMPERATURA MÁXIMA: {ano_max}
    TEMPERATURA MÁXIMA: {temp_max}
    ANO DA TEMPERATURA MINIMA: {ano_min}
    TEMPERATURA MINIMA: {temp_min}
    ESTADO: {estado}
    '''
    
    print(resultado)
            
def verifica_estado(temp_first, temp_second):
    if temp_first > temp_second:
        return 'Diminuiu'
    elif temp_first < temp_second:
        return 'Aumentou'
    else:
        return 'Não aconteceu nada'
    
main()