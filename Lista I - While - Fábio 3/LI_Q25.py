import os
import utils

def main():
    utils.clear()
    print("===========ELEIÇÕES=================")


    eleitores = utils.obter_numero_inteiro("Quantidade de eleitores: ")

    voto1, voto2, voto3, nulo, branco = urna_eletronica(eleitores)

    vencedor(voto1, voto2, voto3)

def urna_eletronica(eleitores):
    voto1 = 0
    voto2 = 0
    voto3 = 0
    nulo = 0
    branco = 0
    contador = 0

    while contador < eleitores:
        utils.clear()
        print("===========ELEIÇÕES=================")
        print("""
Vote 1 --> Johnny Joestar
Vote 2 --> Giorno Giovanna
Vote 3 --> Jolyne Kujo 
Vote 9 --> voto nulo
Vote 0 --> voto em branco  
        """)
        voto = utils.obter_numero_inteiro("Qual número você deseja votar: ")

        if voto == 1:
            voto1 += 1
        elif voto == 2:
            voto2 += 1
        elif voto == 3:
            voto3 += 1
        elif voto == 9:
            nulo += 1
        elif voto == 0:
            branco += 1
        else:
            print("Inválido")

        contador += 1
        utils.clear()

    return voto1, voto2, voto3, nulo, branco



def vencedor(voto1, voto2, voto3):
    if voto1 > voto2 and voto1 > voto3:
        utils.tela_johhny()
    elif voto2 > voto1 and voto2 > voto3:
        utils.tela_giorno()
    elif voto3 > voto1 and voto3 > voto2:
        utils.tela_jolyne()
    else:
        print("empate")
   
   
    #elif empate(voto1, voto2, voto3):
    #    utils.clear()
    #    print("Houve empate! Refazendo eleição.")
    #    v1, v2, v3, nulo, branco = urna_eletronica(qts_eleitores)
    #    vencedor(qts_eleitores, v1, v2, v3, nulo, branco)

#def empate(voto1: int, voto2: int, voto3: int):
#    return voto1 == voto2 or voto1 == voto3 or voto2 == voto3

main()
