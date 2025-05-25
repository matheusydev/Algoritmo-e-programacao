import utils
def main():
    nome = utils.obter_string("Insira um nome: ")
    tamanho = len(nome)

    if tamanho % 2 == 0:
        par(tamanho)
    else:
        impar(tamanho)

def par(tamanho):
    num = tamanho

    while num <= (tamanho ** 2 ):
        print(num)
        num += tamanho


def impar(tamanho):
    num = tamanho
    
    while num != 0:
        if tamanho % num == 0:
            print(num)
        num -= 1


main()