import utils
import os
def main():
    utils.clear()
    print("================== FAZENDA NOVO HORIZONTE ==================") 
    print("=================== VAMOS PESAR OS BOIS? ==================") 
    fichas = utils.obter_numero_inteiro("Quantidade de bois: ")
    utils.clear()


    classifica_boi(fichas)

def classifica_boi(fichas):
    contador = 0
    peso_boi = 0
    boi_mais_gordo = 0
    num_boi_gordo = 0
    boi_mais_magro = 99999
    num_boi_magro = 0
    nome_boi = None
    nome_boi_gordo = None
    nome_boi_magro = None

    while contador < fichas:
        num_boi = utils.obter_numero_inteiro("Insira o Número do boi: ")
        peso_boi = utils.obter_numero_real("Insira o Peso do boi: ")
        nome_boi = utils.obter_string("Insira o nome do boi: ")
        utils.clear()
        if peso_boi > boi_mais_gordo:
            boi_mais_gordo = peso_boi
            num_boi_gordo = num_boi
            nome_boi_gordo = nome_boi

        if peso_boi < boi_mais_magro:
            boi_mais_magro = peso_boi
            num_boi_magro = num_boi
            nome_boi_magro = nome_boi
     
        contador += 1

    print(f"""
================== RESULTADO ==================

------- GORDO -------
Nome = {nome_boi_gordo}
peso = {boi_mais_gordo:.2f} KG
numero = {num_boi_gordo}

------- MAGRO -------
Nome = {nome_boi_magro}
peso = {boi_mais_magro:.2f} KG
numero = {num_boi_magro}

""")






main()