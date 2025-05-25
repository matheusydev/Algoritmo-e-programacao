import q1_number_utils
import utils
def main():
    utils.clear()
    print("---------------- Calcular Primos de N a M ---------------- ")
    n = q1_number_utils.obter_numero_inteiro("Insira o primeiro número: ")
    m = q1_number_utils.obter_numero_inteiro_minimo("Insira o segundo número: ", n + 2)
    utils.clear()

    print("====================== Resultado ======================")
    def verifica_primo(num):
        if num < 2:
            return False
        ctrl = 2
        while ctrl * ctrl <= num:
            if num % ctrl == 0:
                return False
            ctrl += 1
        return True
    
    while n <= m:
        if verifica_primo(n):
            print(f"{n} é primo")
        else:
            print(f"{n} não é primo")
        n += 1

    print("Fim")


main()