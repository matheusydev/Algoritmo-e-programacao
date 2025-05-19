from random import randint
import utils
import time

def main():
    tamanho = utils.obter_numero_inteiro('Insira o tamanho da senha: ')

    senha = gerar_senha(tamanho)
    print(f'A senha gerada é: {senha}')
    delay(1000)

    resultado = utils.obter_numero_inteiro('Você gostou? 1 -> Sim, 2 -> Não: ')

    while resultado != 1:
        print('Tudo bem! Vou gerar uma nova pra você.')
        delay(1000)
        senha = gerar_senha(tamanho)
        print(f'Aqui a nova senha: {senha}')
        delay(1000)
        resultado = utils.obter_numero_inteiro('Você gostou? 1 -> Sim, 2 -> Não: ')

    print(f'Que bom que você gostou! Senha final: {senha}')
    delay(1000)


def gerar_senha(tamanho: int):
    senha = ''
    anterior = ''
    while len(senha) < tamanho:
        atual = str(randint(0, 9))

        if anterior == '' or (atual != anterior and diferenca(atual, anterior) > 1):
            print('.', end='')
            anterior = atual
            senha = senha + atual
        else:
            delay(1000)
    print()
    return senha

def diferenca(valor1: str, valor2: str) -> int:
    return abs(int(valor1) - int(valor2))

def delay(duration: int):
    time.sleep(duration / 1000)

main()
