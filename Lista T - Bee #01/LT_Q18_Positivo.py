def main():
    contador = 0

    for _ in range(6):
        entrada = float(input())
        if entrada > 0:
            contador += 1

    print(f'{contador} valores positivos')       
main()