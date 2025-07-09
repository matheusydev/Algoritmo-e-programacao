def main():
    
    N = int(input())
    for i in range(N):
        entrada = input().split()
        num1 = int(entrada[0]) 
        num2 = int(entrada[1]) 

        if(num2 == 0):
            print("divisao impossivel")
        else:
            resultado = num1 / num2
            print(f"{(resultado):.1f}")

main()