def main():
    N = int(input())

    for _ in range(N):
        entrada = input().split()
        num1 = int(entrada[0])
        num2 = int(entrada[1])
        
        if num1 > num2:
            num1, num2 = num2, num1
        
        soma = 0
        
        for num in range(num1 + 1, num2):
            if num % 2 != 0:  
                soma += num
                
        print(soma)
    

main()