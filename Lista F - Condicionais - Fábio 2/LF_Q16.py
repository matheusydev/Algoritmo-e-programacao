from functions import obter_numero_real

def main():

    nota1 = obter_numero_real("Insira a primeira nota: ")
    nota2 = obter_numero_real("Insira a segunda nota: ")

    calcula_media(nota1, nota2)


def calcula_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 7:
        return print("Aprovado")
    else:
        print("Você vai para o exame final")
        return exame_final(media)


def exame_final(media):
    examefinal = obter_numero_real("Insira a nota do exame final: ")
    mediafinal = (media + examefinal) / 2
    if mediafinal >= 5:
        return print("Aprovado")
    else:
        return print("reprovado")



main()