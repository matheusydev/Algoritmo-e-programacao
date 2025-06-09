def main():

    horas = int(input('Insira a quantidade de horas: '))
    limite_temp = int(input('Insira o limite de temperatura: '))
    maior_temp = None
    menor_umid = None
    contador = 0
    for hora in range(1, horas+1, 1):
        temp = float(input('Insira a temperatura: '))
        umid = float(input('Insira a umidade: '))
        
        maior_temp = verifica_maior_temp(maior_temp, temp)
        menor_umid = verifica_menor_umid(menor_umid, umid)

        if limite_temp > temp:
            contador += 1

print(f'''
''')




def verifica_maior_temp(maior_temp, temp):
    if maior_temp == None or temp < maior_temp:
        maior_temp = temp

def verifica_menor_umid(menor_umid, umid):
    if menor_umid == None or umid > menor_umid:
        menor_umid = umid
        


main()