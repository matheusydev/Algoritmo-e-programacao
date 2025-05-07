from io_utils import obter_numero_real

def main():

    nota1 = obter_numero_real('Insira a primeira nota: ')
    nota2 = obter_numero_real('Insira a segunda nota: ')
    nota3 = obter_numero_real('Insira a terceita nota: ')



    media = calcular_media(nota1, nota2, nota3)

    print(f'A média foi de {media}')

    if nota1 == 0.0 or nota2 == 0.0 or nota3 == 0.0 or media < 5.0:
        print('reprovado')
    elif media < 7.0:
        print('recuperação')
    else:
        print('aprovado')

def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

main()