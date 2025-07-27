import utils
import random
def main():

    frases = ["Olá {nome}, boas férias e volte logo.",
            "Oi {nome}, você vai para a praia na férias.?",
            "Eae {nome}, tá curtindo as férias.",
            "Fala {nome}, relaxe mas também estude.",
            'Tudo bão {nome}, como tá as férias?',
            "{nome}, tudo em cima? ta curtindo as férias?",
            "olha {nome}, nessas férias se beber não dirija.",
            "meu brother {nome}, você vai para o interior comer uma galinha caipira nas férias?",
            "salve {nome}, durante as férias recomendo visitar os parentes",
            "mestre {nome}, você vai conhecer uma cidade nova nas ferias?",
            ]
    
    nome = utils.obter_string("Insira seu nome: ")
    
    frase_escolhida = random.choice(frases)
    frase_personalizada = frase_escolhida.format(nome=nome)

    print(frase_personalizada)
    

main()