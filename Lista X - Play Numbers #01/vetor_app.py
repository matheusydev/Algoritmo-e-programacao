import utils
import vetor_funcionalidades
import vetor_utils

def main():
    
    utils.inicializar()

    colecao = []

    while True:
        menu = ''' >>>>>>>>>> PlayNumbers <<<<<<<<<<
        1. Inicializar Vetor Numérico
        2. Mostrar todos os valores
        3. Resetar Vetor (pedir valor número padrão)
        4. Ver quantidade de itens no vetor
        5. Ver Menor e Maior valores e suas posições
        6. Somatório dos Valores
        7. Média dos Valores
        8. Mostrar Valores Positivos e Quantidade
        9. Mostrar Valores Negativos e Suas Quantidades
        10. Atualizar todos os valores por uma das regras
        11. Adicionar Novos Valores
        12. Remover Itens por Valor exato
        13. Remover por Posição
        14. Editar valor específico por Posição
        15. Salvar valores em um novo arquivo
        16. Sair (salvar valores automaticamente ao sair)
    
>>>>>> '''

        opcao = utils.obter_numero_inteiro_faixa(menu, 1, 16)

        if opcao == 1:
            colecao = vetor_funcionalidades.inicializar_vetor_numerico()
            utils.enter_to_continue()
        elif opcao == 2:
            vetor_funcionalidades.exibir_valorer(colecao)
            utils.enter_to_continue()
        elif opcao == 3:
            colecao = vetor_funcionalidades.resetar_vetor(colecao)
            utils.enter_to_continue()
        elif opcao == 4:
            vetor_funcionalidades.exibir_tamanho(colecao)
            utils.enter_to_continue()
        elif opcao == 5:
            vetor_funcionalidades.maior_e_menor(colecao)
            utils.enter_to_continue()
        elif opcao == 6:
            print(f"{vetor_funcionalidades.somatorio(colecao)}")
            utils.enter_to_continue()
        elif opcao == 7:
            print(f"{vetor_funcionalidades.obter_media(colecao)}")
            utils.enter_to_continue()
        elif opcao == 8:
            vetor_funcionalidades.exibir_valores_positivos(colecao)
            utils.enter_to_continue()
        elif opcao == 9:
            vetor_funcionalidades.exibit_valores_negativos(colecao)
            utils.enter_to_continue()
        elif opcao == 10:
            colecao = vetor_funcionalidades.atualizar_com_regra(colecao)
            utils.enter_to_continue()
        elif opcao == 11:
            colecao = vetor_funcionalidades.adicionar_valor(colecao)
            utils.enter_to_continue()
        elif opcao == 12:
            colecao = vetor_funcionalidades.remover_item(colecao)
            utils.enter_to_continue()
        elif opcao == 13:
            colecao = vetor_funcionalidades.remover_por_posicao(colecao)
            utils.enter_to_continue()
        elif opcao == 14:
            colecao = vetor_funcionalidades.adicionar_posicao(colecao)
            utils.enter_to_continue()
        elif opcao == 15:
            nome_do_arquivo = input("Insira o nome do arquivo: ")
            vetor_funcionalidades.salvar_valores(colecao, nome_do_arquivo)
            utils.enter_to_continue()
        elif opcao == 16:
            vetor_funcionalidades.salvar_sair(colecao, 'backup.txt')
            utils.enter_to_continue()
            break



main()