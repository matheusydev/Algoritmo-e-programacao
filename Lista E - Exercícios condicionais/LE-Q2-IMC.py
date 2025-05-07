from io_utils import obter_numero_real

def main():

    peso = obter_numero_real('Insira seu peso: ')
    altura = obter_numero_real('Insira sua altura: ')

    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    print(f'seu IMC é de {imc:.2f}, você está classificado como {classificacao}.')


def calcular_imc(peso: float, altura: float):
    return peso / (altura ** 2)


def classificar_imc(imc):
   if imc < 18.5:
    return 'Abaixo do Peso'
   elif imc <= 24.9:
    return 'Peso Normal'
   elif imc <= 29.9:
    return 'Sobrepeso'
   elif imc <= 34.9:
    return 'Obesidade Grau I'
   elif imc <= 39.9:
    return 'Obesidade Grau II'
   else:
    return 'Obesidade Grau III'


main()