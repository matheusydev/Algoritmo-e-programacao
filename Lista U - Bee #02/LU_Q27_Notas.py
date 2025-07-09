def main():
        while True:
            nota1 = pedir_nota()
            nota2 = pedir_nota()
            media = (nota1 + nota2) / 2
            print(f"media = {media:.2f}")
            while True:
                print("novo calculo (1-sim 2-nao)")
                opcao = int(input())
                if opcao == 1:
                    break
                elif opcao == 2:
                    return 

def pedir_nota():
    while True:
            nota = float(input())
            if 0 <= nota <= 10:
                return nota
            else:
                print("nota invalida")
main()