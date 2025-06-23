def main():
    entrada = input().split()

    num1 = int(entrada[0])
    num2 = int(entrada[1])
    num3 = int(entrada[2])

    menor = num1
    if num2 < menor:
        menor = num2
    if num3 < menor:
        menor = num3

    maior = num1
    if num2 > maior:
        maior = num2
    if num3 > maior:
        maior = num3

    meio = num1 + num2 + num3 - maior - menor
        
    
    print(f"{menor}")
    print(f"{meio}")
    print(f"{maior}")
    print("")
    print(f"{num1}")
    print(f"{num2}")
    print(f"{num3}")
main()