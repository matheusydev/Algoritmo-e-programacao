def main():
    
    divida = float(input("Insira o valor da dívida: "))
    taxa_mensal = (float(input("Insira o valor do juros em porcenteagem(%): ")) / 100)
    meses = int(input("Insira quantos meses para pagamento: "))

    soma_pagamento = 0
    juros = divida * taxa_mensal
    divida_total = divida + juros

    for _ in range(1, meses+1):
        print(f'=============== {_}° Pagamento ===============')
        print(f'Você está devendo R${divida_total:.2f}')
        pagamento = float(input('Insira o quanto você vai pagar esse mês: '))

        soma_pagamento += pagamento
        divida_total = divida_total - soma_pagamento
        

        if divida_total <= 0:
            print(f'Divida paga com sucesso, no mês {_}')
            break
        
        print(f'Sua divida ainda não foi paga')
        print(f'Ainda falta {meses - _} e falta R${divida_total}')
    
    print("FIM")

        

main()