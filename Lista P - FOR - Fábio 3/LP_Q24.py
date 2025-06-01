# A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e,
# número de filhos. Escreva um algoritmo que leia o salário e o número de filhos de N habitantes e 
# escreva: 
# a) média de salário da população; 
# b) média de número de filhos; 
# c) percentual de pessoas com salário de até R$ 1.000,00

def main():

    entrevistado = int(input("Insira a quantidade de pessoas entrevistada: "))
    total_salario = 0
    total_filha = 0
    baixa_renda = 0

    for i in range(1, entrevistado + 1):
        print(f"Entrevistado {i}")
        salario = float(input("Insira o seu sálario: "))
        filha = int(input("Insira a quantidade de filhos: "))

        total_salario += salario
        total_filha += filha

        if salario < 1000:
            baixa_renda += 1
    
    media_filho = total_filha / entrevistado
    media_salario = total_salario / entrevistado

    resultado = f"""================ OI MALU, TUDO BOM? ================
total de entrevistado: {entrevistado}
media sálarial: {media_salario:.2f}
media de filhos: {media_filho}
sálario inferior a r$: 1000: {baixa_renda}
"""

    print(resultado)
main()