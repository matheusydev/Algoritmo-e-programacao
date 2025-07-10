import utils
import vetor_utils
import random


# i. Inicializar Vetor Numérico
def inicializar_vetor_numerico():
    menui = '''>>>>>>>>>> OPÇÕES <<<<<<<<<

    1 - Gerar dados automático
    2 - Colocar dados manualmente
    3 - Pegar do arquivo

    >>>>> '''

    colecao = []
    opcao = utils.obter_numero_inteiro_faixa(menui, 1, 3)
    if opcao == 1:
        tamanho = utils.obter_numero_inteiro("Insira o tamanho da lista: ")
        minimo = utils.obter_numero_inteiro("Insira o valor minimo da lista: ")
        maximo = utils.obter_numero_inteiro("Insira o valor maximo da lista: ")
        colecao = vetor_utils.gerar_lista(tamanho, minimo, maximo)
        return colecao
    
    elif opcao == 2:
        tamanho = utils.obter_numero_inteiro("Insira o tamanho da lista: ")
        for _ in range(tamanho):
            item = utils.obter_numero_inteiro("Insira o número: ")
            vetor_utils.adicionar(colecao, item)
        return colecao
    
    elif opcao == 3:
        arquivo = open("backup.txt")
        for item in arquivo:
            colecao.append(item)
        return colecao
        

    
# ii. Mostrar todos os valores
def exibir_valorer(colecao):
    print(colecao)
# iii. Resetar Vetor (pedir valor número padrão)
def resetar_vetor(colecao):
    numero = utils.obter_numero_inteiro("Insira o número que deseja substituir todos da lista: ")
    for item in colecao:
        index = colecao.index(item)
        colecao[index] = numero
    return colecao

# iv. Ver quantidade de itens no vetor
def exibir_tamanho(colecao):
    print(f"{len(colecao)}")
# v. Ver Menor e Maior valores e suas posições
def maior_e_menor(colecao):
    index_maior = None
    index_menor = None
    maior = None
    menor = None
    for item in colecao:
        if maior == None or item > maior:
            maior = item
            index_maior = colecao.index(item)

        if menor == None or item < menor:
            menor = item
            index_menor = colecao.index(item)
    
    resultado = f'''
    Maior:{maior} Index:{index_maior}
    Menor:{menor} Index:{index_menor}
    '''
    print(resultado)

# vi. Somatório dos Valores
def somatorio(colecao):
    somatorio = 0

    for item in colecao:
        somatorio += item

    return somatorio

# vii. Média dos Valores
def obter_media(colecao):
    somatorio = 0
    denominador = len(colecao)
    for item in colecao:
        somatorio += item
    
    resultado = somatorio / denominador
    return resultado

# viii. Mostrar Valores Positivos e Quantidade
def exibir_valores_positivos(colecao):
    contador = 0
    for item in colecao:
        if item > 0:
            print(item)
            contador += 1
    print(f"{contador} Numeros positivos")
    
# ix. Mostrar Valores Negativos e Suas Quantidades
def exibit_valores_negativos(colecao):
    contador = 0
    for item in colecao:
        if item < 0:
           print(item)
           contador += 1
    print(f"{contador} numeros Negativos")
# x. Atualizar todos os valores por uma das regras:
def atualizar_com_regra(colecao):
    menux = '''>>>>>>>>>> REGRA <<<<<<<<<

    1 - Multiplicar por um valor
    2 - Elevar a um valor
    3 - Reduzir a uma fração
    4 - Substituir valores negativos por um número aleatórios da uma faixa
    5 - Ordenar valores 
    6 - Embaralhar valores

    >>>>> '''
    
    opcao = utils.obter_numero_inteiro_faixa(menux, 1, 6)

    if opcao == 1:
        valor = utils.obter_numero_inteiro("Insira o valor que você deseja multiplicar: ")
        nova_colecao = vetor_utils.mapear(colecao, vetor_utils.multiplicar, valor)
        print(nova_colecao)
    elif opcao == 2:
        valor = utils.obter_numero_inteiro("Insira o valor que você deseja elevar: ")
        nova_colecao = vetor_utils.mapear(colecao, vetor_utils.potencia, valor)
        print(nova_colecao)
    elif opcao == 3:
        numerador, denominador = map(int, "Insira a fração").split("/")
        fracao = numerador / denominador
        print(f'{vetor_utils.reduzir_fracao(fracao, colecao)}')
    elif opcao == 4:
        minimo, maximo = map(int, "Insira o valor minimo e o maximo").split()
        colecao = vetor_utils.substituir_valor(colecao, minimo, maximo)
        print(colecao)
    elif opcao == 5:
        alternativa = '''>>>>>>>>>> REVERSE <<<<<<<<<

        1 - Cresente
        2 - Decrescente

        >>>>> '''
        opcao = utils.obter_numero_inteiro_faixa(alternativa, 1, 2)

        if opcao == 1:
            colecao = vetor_utils.ordenar_crescente 
            print(colecao)
        elif opcao == 2:
            colecao = vetor_utils.ordenar_decrescente
    elif opcao == 6:
        colecao = vetor_utils.embaralhar(colecao)
        print(colecao)

# xi. Adicionar Novos Valores
def adicionar_valor(colecao):
    valor = utils.obter_numero_inteiro("Insira o nova volor a ser inserido: ")
    nova_colecao = vetor_utils.adicionar(colecao, valor)
    return nova_colecao
# xii. Remover Itens por Valor exato
def remover_item(colecao):
    valor = utils.obter_numero_inteiro("Insira o valor que deseja ser removido: ")
    for item in colecao:
        if item == valor:
            indice = colecao.index(item)
            colecao.pop(indice)
    return colecao

# xiii. Remover por Posição
def remover_por_posicao(colecao):
    index = utils.obter_numero_inteiro("Insira o indice para remover: ")
    colecao.pop(index)
    return colecao
# xiv. Editar valor específico por Posição
def adicionar_posicao(colecao):
    valor = utils.obter_numero_inteiro("Insrira o valor: ")
    index = utils.obter_numero_inteiro("Insira o indice: ")
    colecao.insertion(valor, index)
    return colecao
# xv. Salvar valores em arquivo 
def salvar_valores(colecao, nome_do_arquivo):
    arquivo = open(nome_do_arquivo, 'a')
    linha_do_arquivo = ''

    for item in colecao:
        linha_do_arquivo += f'{item}'

    arquivo.write(linha_do_arquivo)

# xvi. Sair (salvar valores automaticamente ao sair)
def salvar_sair(colecao, backup):
    salvar_valores(colecao, "backup.txt")
    print("Arquivos Salvos com sucesso")