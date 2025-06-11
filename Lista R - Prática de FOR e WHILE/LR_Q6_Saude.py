# ● Contexto/Problema: Um treinador pessoal precisa monitorar o progresso de seus clientes em um
# determinado exercício ao longo de várias sessões. Para cada sessão de treino, o programa deve
# registrar o número de repetições realizadas e o peso levantado. O programa deve ser capaz de calcular
# o volume total (peso * repetições) para cada sessão e, ao final, identificar a sessão com o maior volume
# e a tendência de melhora (se o volume médio da segunda metade das sessões é maior que o da
# primeira metade).
# ● Entrada: O usuário deve informar a quantidade de sessões de treino para análise. Para cada sessão, o
# usuário deve informar o número de repetições e o peso levantado.
# ● Saída Esperada: Para cada sessão, o volume total. Ao final, indicar a sessão (pelo seu número ou
# identificador) com o maior volume e uma mensagem sobre a tendência de melhora (por exemplo,
# "" ou "").
def main():
    
    sessoes = int(input('Insira a quantidade de sessões: '))
    total_volume = 0
    first_volume = 0
    second_volume = 0
    metade = sessoes // 2
    maior_volume = 0
    auge = 0

    for sessao in range(1, sessoes + 1):
        print(f'sessão {sessao}')    
        peso = int(input('Insira o peso: '))
        repeticao = int(input('Insira a quantidade de repetição: '))
        total_volume = (peso * repeticao)
        if total_volume > maior_volume:
            maior_volume = total_volume
            auge = sessao

        if sessao <= metade:
            first_volume += total_volume
        else:
            second_volume += total_volume

    media_first = first_volume / metade
    media_second = first_volume / (sessoes - metade)
        
    resultado = verifica_resutado(first_volume, second_volume)

    menu = f'''
Resultado {resultado}
maior volume: {maior_volume}
melhor sessão: {auge}
media da primeira metade: {media_first:.2f}
media da segunda metade: {media_second:.2f}
'''

    print(menu)

def verifica_resutado(first_volume, second_volume):
    if first_volume > second_volume:
        return 'Tendência de melhora observada'
    else:
        return 'Não houve melhora significativa'
main()