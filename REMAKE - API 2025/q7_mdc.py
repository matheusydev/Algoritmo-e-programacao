import utils
def main():
    print("--------------- Calcular MDC ---------------")
    num1 = utils.obter_numero_inteiro("Insira um número inteiro para calcular: ")
    num2 = utils.obter_numero_inteiro("Insira um outro número inteiro: ")

    main_num1 = num1
    main_num2 = num2

    while num2 != 0:

        resto = num1 % num2
        num1 = num2
        num2 = resto
        
    print(f"O MDC é de {main_num1} e {main_num2} é {num1}")

main()