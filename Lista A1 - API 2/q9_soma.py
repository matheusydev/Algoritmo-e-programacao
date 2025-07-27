import utils
def main():

    referencia = utils.obter_numero_faixa("Insira o valor de referência: ", 1, 99)
    somatorio = referencia

    num = None
    while num != referencia:
        num = utils.obter_numero_faixa("Insira qualquer valor entre 1 e 99: ", 1, 99)

        if num % referencia == 0:
            somatorio += num

    print(f"O somatório dos valores múltiplos é {somatorio}")

main()