# Contexto/Problema: Para um controle financeiro mais rigoroso, é necessário registrar todas as
# receitas e despesas de um mês. O programa deve permitir que o usuário insira múltiplas receitas e
# múltiplas despesas. Para cada transação (seja receita ou despesa), o usuário deve informar uma
# descrição e o valor. Ao final, o programa deve apresentar o total de receitas, o total de despesas, o
# saldo final do mês e categorizar a despesa de maior valor e a receita de maior valor.
# ● Entrada: O usuário deve informar a quantidade de receitas a serem cadastradas e, para cada uma, a
# descrição e o valor. Em seguida, o usuário deve informar a quantidade de despesas a serem
# cadastradas e, para cada uma, a descrição e o valor.
# ● Saída Esperada: O total de receitas, o total de despesas, o saldo final do mês. A descrição e o valor da
# maior receita e da maior despesa


def main():

    qtd_despesa = int(input("Insira a quantidade de Despesas: "))
    qtd_receita = int(input("Insira a quantidade de Receita: "))
    soma_despesa = 0
    soma_receita = 0
    maior_despesa = None
    maior_receita = None
    despesa_descricao = ""
    receita_descricao = ""
    

    for _ in range(1, qtd_despesa + 1):
        print(f"Despesa {_}")
        despesa = float(input("Insira o valor da despesa: "))
        descricao = str(input("Insira a descrição da despera: "))

        soma_despesa += despesa

        if maior_despesa is None or despesa > maior_despesa:
            maior_despesa = despesa
            despesa_descricao = descricao


    for _ in range(1, qtd_receita + 1):
        print(f"Receita {_}")
        receita = float(input("Insira o valor da receita: "))
        descricao = str(input("Insira a descrição da despera: "))

        soma_receita += receita

        if maior_receita is None or receita > maior_receita:
            maior_receita = receita
            receita_descricao = descricao

    saldo = soma_receita - soma_despesa
        

    print(f"""=============== RESULTADO ===============
Quantidade de Receita: {qtd_receita}
Quantidade de Despesa: {qtd_despesa}
-----------------------------------------------------------
Maior Receita: {maior_receita}
Descrição: {receita_descricao}
-----------------------------------------------------------
Maior Despesa: {maior_despesa}
descrição: {despesa_descricao}
-------------------------------------------------
Saldo: {saldo}
==========================================================
""")



main()