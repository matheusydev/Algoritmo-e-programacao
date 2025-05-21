def obter_numero_real(label: str):
    entrada = input(label)
    try:
        numero = float(entrada)
        return numero
    except ValueError:
        print(f'O que você colocou "{entrada}" não é um número real')
        return obter_numero_real(label)