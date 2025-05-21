import math
import turtle


def square(t, length):
    """Desenha um quadrado com lados do tamanho especificado."""
    for i in range(4):  # Repetimos 4 vezes para desenhar os 4 lados do quadrado
        t.fd(length)    # Move o turtle para frente
        t.lt(90)        # Gira 90 graus para a esquerda



def polyline(t, n, length, angle):
    """Desenha uma sequência de segmentos de linha (polilinha).

    t: objeto turtle
    n: número de segmentos
    length: comprimento de cada segmento
    angle: ângulo entre os segmentos
    """
    for i in range(n):
        t.fd(length)    # Move o turtle para frente
        t.lt(angle)     # Gira para a esquerda com o ângulo especificado


def polygon(t, n, length):
    """Desenha um polígono regular com n lados."""
    angle = 360.0 / n       # Ângulo interno de cada vértice
    polyline(t, n, length, angle)  # Usa a função polyline para desenhar o polígono


def arc(t, r, angle):
    """Desenha um arco com raio r e ângulo especificado."""
    arc_length = 2 * math.pi * r * abs(angle) / 360  # Calcula o comprimento total do arco
    n = int(arc_length / 4) + 3                      # Número de segmentos para suavizar o arco
    step_length = arc_length / n                     # Tamanho de cada segmento
    step_angle = float(angle) / n                    # Ângulo entre os segmentos

    # Faz uma leve curva inicial para melhorar a precisão visual do arco
    t.lt(step_angle / 2)
    polyline(t, n, step_length, step_angle)          # Desenha o arco como uma polilinha
    t.rt(step_angle / 2)                             # Corrige a orientação no final


def circle(t, r):
    """Desenha um círculo com raio r."""
    arc(t, r, 360)  # Um círculo é um arco com 360 graus


# Este bloco só é executado se o script for executado diretamente (não importado)
if __name__ == '__main__':
    bob = turtle.Turtle()  # Cria um novo turtle chamado bob

    # Move o turtle para a posição inicial sem desenhar
    radius = 100
    bob.pu()        # Levanta a caneta (pen up)
    bob.fd(radius)  # Move-se para frente até a borda do círculo
    bob.lt(90)      # Gira para cima
    bob.pd()        # Abaixa a caneta (pen down)

    # Desenha um círculo com o centro na origem
    circle(bob, radius)

    # Espera o usuário fechar a janela
    turtle.mainloop()