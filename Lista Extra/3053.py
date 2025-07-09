def main():
    movimentos = int(input())
    moeda_posicao = input()

    for _ in range(movimentos):
        tipo_de_movimentos = int(input())

        if tipo_de_movimentos == 1:  
            if moeda_posicao == 'A':
                moeda_posicao = 'B'
            elif moeda_posicao == 'B':
                moeda_posicao = 'A'
        elif tipo_de_movimentos == 2:  
            if moeda_posicao == 'B':
                moeda_posicao = 'C'
            elif moeda_posicao == 'C':
                moeda_posicao = 'B'
        elif tipo_de_movimentos == 3:  
            if moeda_posicao == 'A':
                moeda_posicao = 'C'
            elif moeda_posicao == 'C':
                moeda_posicao = 'A'

    
    print(moeda_posicao)
main()