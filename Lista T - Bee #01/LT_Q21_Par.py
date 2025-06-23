def main():
    contador = 0

    for _ in range(5):
        entrada = int(input())
        if entrada % 2 == 0:
            contador += 1

    print(f'{contador} valores par')       
main()