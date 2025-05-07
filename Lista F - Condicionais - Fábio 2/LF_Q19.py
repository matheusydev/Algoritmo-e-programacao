from functions import obter_numero_real

def main():
    altura = obter_numero_real("Insira a altura: ")
    peso = obter_numero_real("Insira o peso: ")

    imc = calcular_imc(peso, altura)
    classificacao = classificacao_imc(imc)

    print(f'seu IMC é de {imc:.2f} e sua classificação é {classificacao}')

def calcular_imc(peso: float, altura: float):
    return peso / (altura ** 2)

def classificacao_imc(imc: float):
   if imc < 25:
    return 'Normal'
   elif 25 < imc < 30:
    return 'Obeso'
   else:
    return 'Obesidade Mórbida'
   

main()
   