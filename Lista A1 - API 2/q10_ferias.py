import utils
import random

def main():
    nome = utils.obter_string("Insira seu nome: ")
    frase = mensagem(nome)
    print(frase)

def mensagem(nome):
    frases = [
        f"Olá {nome}, boas férias e volte logo.",
        f"Oi {nome}, você vai para a praia nas férias?",
        f"Eae {nome}, tá curtindo as férias.",
        f"Fala {nome}, relaxe mas também estude.",
        f"Tudo bão {nome}, como tá as férias?",
        f"{nome}, tudo em cima? Tá curtindo as férias?",
        f"Olha {nome}, nessas férias se beber não dirija.",
        f"Meu brother {nome}, você vai para o interior comer uma galinha caipira nas férias?",
        f"Salve {nome}, durante as férias recomendo visitar os parentes.",
        f"Mestre {nome}, você vai conhecer uma cidade nova nas férias?"
    ]

    frase_escolhida = random.randint(0, len(frases) - 1)
    return frases[frase_escolhida]

main()
