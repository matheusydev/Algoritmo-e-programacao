def main():
    horas = int(input('Insira a quantidade de horas: '))
    limite_temp = int(input('Insira o limite de temperatura: '))
    maior_temp = None
    menor_umid = None
    contador = 0
    
    for hora in range(1, horas+1):
        temp = float(input('Insira a temperatura: '))
        umid = float(input('Insira a umidade: '))
        
        maior_temp = verifica_maior_temp(maior_temp, temp)
        menor_umid = verifica_menor_umid(menor_umid, umid)

        if temp > limite_temp:
            contador += 1

    print(f'''
Maior temperatura registrada: {maior_temp}
Menor umidade registrada: {menor_umid}
Quantidade de vezes que a temperatura excedeu o limite: {contador}
    ''')


def verifica_maior_temp(maior_temp, temp):
    if maior_temp is None or temp > maior_temp:
        return temp
    return maior_temp

def verifica_menor_umid(menor_umid, umid):
    if menor_umid is None or umid < menor_umid:
        return umid
    return menor_umid

main()
