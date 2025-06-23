def main():
    entrada = input().split()

    num1 = int(entrada[0])
    num2 = int(entrada[1])

    if num1 % num2 ==0 or num2 % num1 == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
        
main()