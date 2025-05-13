def main():
    print('========== CALCULADORA DE TREINO BY MALU E THEUS S2 ==========')
    print('PS: MENÇÃO HONROSA PARA XAMÃ S2')
    peso_atual = float(input("Digite o seu peso atual (kg):"))
    sexo = int(input("Digite seu sexo (MASCULINO = 0 | FEMININO = 1): "))
    perda = float(input("Quantos quilos vocÊ deseja perder?: "))
    dias_por_semana = int(input("Quantos dias por semana irá treinar?: "))
    tempo_por_dia = int(input("Quantas horas por dia irá treinar?: ")) * 60

    proporcao_transport = int(input("Qual a proporção de tempo dedicada ao Transport?: "))/100
    proporcao_escada = 1 - proporcao_transport

    tempo_por_dia_transport = tempo_por_dia * proporcao_transport
    tempo_por_dia_escada = tempo_por_dia * proporcao_escada

    gastar = perda * 7000

    if sexo == 0:
        cal_transport = tempo_por_dia_transport * 100 // 5
        cal_escada = tempo_por_dia_escada * 100 // 7
    else: 
        cal_transport = tempo_por_dia_transport * 100 // 6
        cal_escada = tempo_por_dia_escada * 100 // 8


    gasto_total_dia = cal_transport + cal_escada
     
 
    dias = 0
    
    gasto_necessario_exceder = 0
    if sexo == 0:
        gasto_necessario_exceder = 2400
    else:
        gasto_necessario_exceder += 2000
    
    if gasto_total_dia < gasto_necessario_exceder:
        print("Olha... com esse tempo de treino é mais fácil bater laje e peneirar brita... treina mais pow")
    
    else:
        while gastar > 0:
            gastar += gasto_necessario_exceder
            gastar -= gasto_total_dia 
            dias += 1

        semanas = dias // dias_por_semana
        print(f''' ========== RESULTADO DO TREINO ==========
                    > SEMANAS ATÉ ALCANÇAR O RESULTADO: {semanas}
                    > MINUTOS DE TRANSPORTE POR DIA: {tempo_por_dia_transport: .0f}
                    > MINUTOS DE ESCADA POR DIA: {tempo_por_dia_escada: .0f}
            
        ''')

    

main()
