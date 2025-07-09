def main():
    N = int(input())
    contador = 1

    while contador <= N:
        quadrado = contador**2
        if contador % 2 == 0:
            print(f'{contador}^2 = {quadrado}')
    
        contador +=1
main()