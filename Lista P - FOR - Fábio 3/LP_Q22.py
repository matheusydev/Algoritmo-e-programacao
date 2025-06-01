def main():

    fichas = int(input("Insira a quantidade de consulta: "))
    mais_gordo = None
    mais_magro = None
    ident_gordo = None
    ident_magro = None

    for i in range(1, fichas + 1):
        ident = int(input("Insira o a númeração do boi: "))
        peso = float(input("Insira o peso do boi: "))

        if mais_gordo == None or mais_gordo < peso:
            mais_gordo = peso
            ident_gordo = ident


        if mais_magro == None or mais_magro > peso:
            mais_magro = peso
            ident_magro = ident


    resultado = f"""========================= RESULTADO =========================
------------- GORDO ---------------
peso: {mais_gordo}KG
identificação: {ident_gordo}

------------- MAGRO ---------------
peso: {mais_magro}KG
identificação: {ident_magro}
============================================================
"""

    print(resultado)

main()