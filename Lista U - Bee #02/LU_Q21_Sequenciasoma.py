def main():
    while True:
        entrada = input().split()
        num1 = int(entrada[0]) 
        num2 = int(entrada[1]) 

        if num1 <= 0 or num2 <= 0:
            break
        
        if num1 > num2:
             num1, num2 = num2, num1
        
        soma = 0
        numeros_string_acumulada = ""
        for i in range(num1, num2 + 1):
            numeros_string_acumulada += str(i) + " "  
            soma += i
        
        print(f"{numeros_string_acumulada.strip()} Sum={soma}")


main()