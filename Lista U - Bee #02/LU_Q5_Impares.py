def main():
    N = int(input())
    contador = 1

    while contador <= N:
        if contador % 2 != 0:
            print(f'{contador}')
    
        contador +=1
main()