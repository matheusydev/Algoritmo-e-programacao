from utils import show_menu_5, obter_numero_inteiro, obter_numero_real, obter_string
import os

def main():
    valor = 0
    produto = None
    clear_screen()

    while True:
        clear_screen()
        show_menu_5()
        opcao = obter_numero_inteiro("Insira a opção do menu: ")





def clear_screen():
    os.system('cls')

def enter():
    input("aperte <Enter> para continuar... ")
    clear_screen()
     
    

main()