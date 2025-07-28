def obter_numero(label):
    entrada = input(label)
    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print(f'O que você colocou na entrada "{entrada}" não é um número inteiro válido.')
        return obter_numero(label)
    

def obter_numero_real(label):
    entrada = input(label)
    try:
        numero = float(entrada)
        return numero
    except ValueError:
        print(f'O que você colocou na entrada "{entrada}" não é um número real válido.')
        return obter_numero_real(label)
    

def obter_numero_inteiro_positivo(label):
    entrada = input(label)
    try:
        numero = int(entrada)
        if numero > 0:
            return numero
        else:
            print(f'O número precisa ser positivo.')
            return obter_numero_inteiro_positivo(label)
    except ValueError:
        print(f'O que você colocou na entrada "{entrada}" não é um número inteiro válido.')
        return obter_numero_inteiro_positivo(label)
    

def obter_numero_real_positivo(label):
    entrada = input(label)
    try:
        numero = float(entrada)
        if numero > 0:
            return numero
        else:
            print(f'O número precisa ser positivo.')
            return obter_numero_real_positivo(label)
    except ValueError:
        print(f'O que você colocou na entrada "{entrada}" não é um número válido.')
        return obter_numero_real_positivo(label)
    

def obter_numero_minimo(label, minimo):
    entrada = input(label)
    try:
        numero = int(entrada)
        if numero >= minimo:
            return numero
        else:
            print(f'O número {numero} não é maior ou igual ao mínimo {minimo}.')
            return obter_numero_minimo(label, minimo)
    except ValueError:
        print(f'O que você colocou na entrada "{entrada}" não é um número inteiro válido.')
        return obter_numero_minimo(label, minimo)
    

def obter_numero_faixa(label, minimo, maximo):
    entrada = input(label)
    try:
        numero = int(entrada)  
        if minimo <= numero <= maximo:
            return numero
        else:
            print(f'O valor deve estar entre {minimo} e {maximo}.')
            return obter_numero_faixa(label, minimo, maximo)
    except ValueError:
        print(f'O que você colocou na entrada "{entrada}" não é um número inteiro válido.')
        return obter_numero_faixa(label, minimo, maximo)
    

def obter_numero_faixa_float(label, minimo, maximo):
    entrada = input(label)
    try:
        numero = float(entrada)  
        if minimo <= numero <= maximo:
            return numero
        else:
            print(f'O valor deve estar entre {minimo} e {maximo}.')
            return obter_numero_faixa_float(label, minimo, maximo)
    except ValueError:
        print(f'O que você colocou na entrada "{entrada}" não é um número inteiro válido.')
        return obter_numero_faixa_float(label, minimo, maximo)
    

def obter_string(label):
    return input(label)
