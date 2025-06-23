def main():
    contador = 0
    somatorio = 0

    for _ in range(6):
        entrada = float(input())
        if entrada > 0:
            contador += 1
            somatorio += entrada

        resultado = somatorio / contador

    print(f'{contador} valores positivos')     
    print(f'{resultado:.1f}')  
main()