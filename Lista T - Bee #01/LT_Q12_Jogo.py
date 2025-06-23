def main():
    entrada = input().split()

    hora_ini = int(entrada[0])
    minu_ini = int(entrada[1])
    hora_fim = int(entrada[2])
    minu_fim = int(entrada[3])

    if (hora_fim == hora_ini) and (minu_ini == minu_fim):
        hora = 24
        minuto = 0
    elif (hora_ini == hora_fim) and (minu_ini > minu_fim):
        hora = 23
        minuto = (60 - minu_ini) + minu_fim
    elif (hora_ini == hora_fim) and (minu_ini < minu_fim):
        hora = 0
        minuto = minu_fim - minu_ini
    elif (hora_ini < hora_fim) and (minu_ini < minu_fim):
        hora = hora_fim - hora_ini
        minuto = minu_fim - minu_ini
    elif (hora_ini < hora_fim) and (minu_ini > minu_fim):
        hora = hora_fim - hora_ini - 1
        minuto = (60 - minu_ini) + minu_fim
    elif (hora_ini > hora_fim):
        hora = (24 - hora_ini) + hora_fim
        minuto = minu_fim - minu_ini
        if minu_ini > minu_fim:
            hora = hora - 1
            minuto = (60 - minu_ini) + minu_fim

    print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")
        

main()
