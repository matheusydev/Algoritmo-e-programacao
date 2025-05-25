import os

def clear():
    os.system("cls")

def enter():
    enter = input("Enter para continuar: ")
    clear()

def menu_q6():
    menu = """------------------- Bar do Matheus -------------------
1 - Pedir um produto
2 - Somatorio da conta
3 - Imprimir a conta
4 - Confirmar o pagamento 
0 - Sair
"""
    print(menu)


