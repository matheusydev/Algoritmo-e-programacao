import utils
import os

def main():
    entrevistado = utils.obter_numero_inteiro('Digite a quantidade de habitantes: ')
    
    armazenar_dados(entrevistado)


def armazenar_dados(entrevistado):
    contador = 0
    baixa_renda = 0
    soma_salario = 0
    soma_qtd_filhos = 0

    while contador < entrevistado:
        salario = utils.obter_numero_real('Digite o salário: ')
        qtd_filhos = utils.obter_numero_inteiro('Digite a quantidade de filhos: ')
        print('')
        soma_qtd_filhos += qtd_filhos
        soma_salario += salario
        contador += 1

        if salario <= 1000:
            baixa_renda += 1
        
    media_salario = soma_salario/entrevistado
    media_qtd_filhos = soma_qtd_filhos/entrevistado
    percentual_baixa_renda = (baixa_renda/entrevistado)*100

    print(f'''
- Quantidade de entrevistados: {entrevistado}
- Media do salario: {media_salario:.2f}
- Media da quantidade de filhos: {media_qtd_filhos}
- Percentual de pessoas quantidades: {percentual_baixa_renda:.1f}''')


main()