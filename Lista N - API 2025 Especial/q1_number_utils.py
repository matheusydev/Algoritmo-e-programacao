def obter_numero_inteiro(label):
    valor = input(label)
    try:
        numero = int(valor)
        return numero
    except ValueError:
        print(f'O que você colocou "{valor}" não é um número inteiro válido')
        print("Tente novamente!")
        return obter_numero_inteiro(label)


def obter_numero_inteiro_positivo(label):
    valor = input(label)
    try:
        numero = int(valor)
        if numero > 0:
            return numero
        else:
            print(f'O número "{valor}" não é positivo')
            print("Tente novamente!")
            return obter_numero_inteiro_positivo(label)
    except ValueError:
        print(f'O que você colocou "{valor}" não é um número inteiro válido')
        print("Tente novamente!")
        return obter_numero_inteiro_positivo(label)


def obter_numero_inteiro_minimo(label, valor_min):
    valor = input(label)
    try:
        numero = int(valor)
        if numero > valor_min:
            return numero
        else:
            print(f'O número "{valor}" não é maior que {valor_min}')
            print("Tente novamente!")
            return obter_numero_inteiro_minimo(label, valor_min)
    except ValueError:
        print(f'O que você colocou "{valor}" não é um número inteiro válido')
        print("Tente novamente!")
        return obter_numero_inteiro_minimo(label, valor_min)


def obter_numero_inteiro_maximo(label, valor_max):
    valor = input(label)
    try:
        numero = int(valor)
        if numero < valor_max:
            return numero
        else:
            print(f'O número "{valor}" deve ser menor que {label, valor_max}')
            print("Tente novamente!")
            return obter_numero_inteiro_maximo(label)
    except ValueError:
        print(f'O que você colocou "{valor}" não é um número inteiro válido')
        print("Tente novamente!")
        return obter_numero_inteiro_maximo(label, valor_max)


def obter_numero_inteiro_faixa(label, valor_min, valor_max):
    valor = input(label)
    try:
        numero = int(valor)
        if valor_min <= numero <= valor_max:
            return numero
        else:
            print(f'O número "{valor}" deve estar entre {valor_min} e {valor_max}')
            print("Tente novamente!")
            return obter_numero_inteiro_faixa(label, valor_min, valor_max)
    except ValueError:
        print(f'O que você colocou "{valor}" não é um número inteiro válido')
        print("Tente novamente!")
        return obter_numero_inteiro_faixa(label, valor_min, valor_max)

