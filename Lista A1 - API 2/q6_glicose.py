import utils

def main():
    glicose = utils.obter_numero("Insira o valor da sua glicose em mg/dL: ")
    resultado = verifica_estado(glicose)
    print(f'Seu estado é: {resultado}')

def verifica_estado(glicose):
    if glicose < 100:
        return "Normal"
    elif 100 <= glicose <= 125:
        return "Pré-diabetes"
    else:
        return "Diabetes"

main()
