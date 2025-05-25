#a. Inserir produtos: Cerveja (9 reais), Tira-Gosto (39 reais) e
#Água (5 reais). Entrada: “1 C” significa uma cerveja na
#conta. “3 A” 3 águas.
#b. Calcular a conta, incluindo 10% de taxa de serviço.
#c. Compras acima de 10 cervejas ou valor total superior a 200
#reais ficam isentos dos 10%
#d. Imprimir Conta: Pede quantas pessoas irão pagar.
#i. Valor da Conta e valor por pessoa.
#ii. Valor da taxa de serviço
#iii. Valor Total com taxa de serviço.
#e. Confirmar pagamento: que zera a conta da mesa.


import q1_number_utils
import utils
def main():

    cervejas = 0
    agua = 0
    tira_gosto = 0
    total_C = 0
    total_A = 0
    total_T = 0
    total = 0
    resultado = 0
    imposto = 0

    while True:
        utils.clear
        utils.menu_q6()
        
        opcao = q1_number_utils.obter_numero_inteiro_faixa("Insira uma opção: ", 0, 4)

        if opcao == 1:
            pedido = input()
            qtd = int(pedido.split()[0])
            produto = pedido.split()[1]
            if produto == 'C'.upper():
                cervejas += qtd
            elif produto == 'A'.upper():
                agua += qtd
            elif produto == 'T'.upper():
                tira_gosto += qtd
            else:
                continue
        elif opcao == 2:
            total_C = cervejas * 9
            total_A = agua * 5
            total_T = tira_gosto * 39
            total = (total_C + total_A + total_T)
            if cervejas > 10 or total > 200:
                imposto = 0
                resultado = total + imposto
                print(resultado)
            else:
                imposto = (total * 0.1)
                resultado = total + imposto
                print(resultado)
        elif opcao == 3:
            pessoas = q1_number_utils.obter_numero_inteiro_positivo("Insira a quantidade de pessoas: ")
            valor_individual = resultado / pessoas
            final = conta()
            print(conta)
            utils.enter
            break
        else:
            break

def conta():
    conta = f"""=============== CONTA ===============
    Cervejas: x{cervajas} = R$:{total_C}
    Água: x{agua} = R$:{total_A}
    Tira-Gosto: x{tira_gosto} = R$:{total_T}
    ----------------------------------------
    Total: R$:{total}
    Imposto R$: {imposto}
    Total: R${resultado}
    pessoas: {pessoal}
    valor Individual: {valor_individual}
    ----------------------------------------
"""

main()