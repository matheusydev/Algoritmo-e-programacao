import utils
def main():

    idade = utils.obter_numero_intero_positivo("Insira a sua idade: ")
    peso = utils.obter_numero_real("Insira o seu peso: ")

    resultado = verifica_se_pode_doar(idade, peso)

    print(resultado)

def verifica_se_pode_doar(idade, peso):
    if 18 <= idade <= 60 and peso >= 50:
        return "APTO PARA DOAR"
    else:
        return "INAPTO PARA DOAR" 

    



main()