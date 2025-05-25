import q1_number_utils
def main():

    a = q1_number_utils.obter_numero_inteiro_positivo("Insira um número inteiro positivo: ")
    b = q1_number_utils.obter_numero_inteiro_minimo(f"Insira um número inteiro de no minimo {a + 11}: ", a + 11)

    def contador_divisor(num):
        contador = 0
        ctrl = 1
        while ctrl <= num:
            if num % ctrl == 0:
                contador += 1
            ctrl += 1
        return contador


    while a <= b:
        divisores = contador_divisor(a)
        print(f"{a} tem ({divisores}) devisores")
        a +=1 


    
main()