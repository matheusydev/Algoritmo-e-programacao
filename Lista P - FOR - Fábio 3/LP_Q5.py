def main():
    num = int(input("Insira um valor para calcular o fatorial: "))
    fatorial = 1 

    for i in range(1, num, 1):
        fatorial *= i    

    print(f" {num}! = {fatorial}")

main()
                  
