def obter_nome(label):
    nome = input(label)


def obter_nome_min(label):
    min = int(input("Insira o valor mínimo: "))
    nome = input(label)
    tamanho = len(nome)
    if tamanho > min:
        return nome
    else:
        print(f"O {nome} é inferior ao mínimo de {max}")
        print("Tente novamente! ")
        return obter_nome_min(label)
    

def obter_nome_max(label):
    max = int(input("Insira o valor máximo: "))
    nome = input(label)
    tamanho = len(nome)
    if tamanho < max:
        return nome
    else:
        print(f"O {nome} ultrapassou o tamanho máximo de {max}")
        print("Tente novamente! ")
        return obter_nome_max(label)
    
def obter_nome_faixa(label):
    min = int(input("Insira o valor mínimo: "))
    max = int(input("Insira o valor máximo: "))
    nome = input(label)
    tamanho = len(nome)
    if min < tamanho < max:
        return nome
    else:
        print(f"O {nome} deve está entre {min} e {max}")
        print("Tente novamente! ")
        obter_nome_faixa(label)