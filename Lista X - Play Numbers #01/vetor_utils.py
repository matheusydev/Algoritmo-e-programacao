import random
import utils

def gerar_lista(tamanho, minimo, maximo):
    colecao = []

    for _ in range(tamanho):
        colecao.append(random.randint(minimo, maximo))

    return colecao


def adicionar(colecao, item):
    colecao.append(item)
    return colecao


def remover(colecao, valor):
    nova_colecao = []

    for item in colecao:
        if item != valor:
            nova_colecao.append(item)
    
    return nova_colecao


def mapear(colecao, funcao_transformadora, valor):
    nova_colecao = []

    for item in colecao:
       item_transformado = multiplicar(item, valor)
       nova_colecao.append(item_transformado)

    return nova_colecao

def filtrar(colecao, criterio):
    nova_colecao = []

    for item in colecao:
        if criterio(item):
            nova_colecao.append(item)

    return nova_colecao

def reduzir(colecao, redutora, inicial):
    acumulado = inicial

    for item in colecao:
        acumulado = redutora(acumulado, item)

    return acumulado

def mostrar(colecao):
    for item in colecao:
        print(item)


def multiplicar(num1, num2):
    resultado = num1 * num2
    return resultado

def potencia(num, potencia):
    resultado = num ** potencia
    return resultado

def reduzir_fracao(fracao, colecao):
    somatorio = 0

    for item in colecao:
        item_fracao = item * fracao
        somatoria += item_fracao

        return somatorio
    
def substituir_valor(colecao, minimo, maximo):

    for item in colecao:
        if item > 0:
            index = colecao.index(item)
            colecao[index] = random.randint(minimo, maximo)

    return colecao
            
def ordenar_crescente(colecao):
    crescente = colecao.sort()
    return crescente

def ordenar_decrescente(colecao):
    decrescente = colecao.sort(reversed=True)
    return decrescente

def embaralhar(colecao):
    colecao_embaralhada = random.shuffle(colecao)
    return colecao_embaralhada

