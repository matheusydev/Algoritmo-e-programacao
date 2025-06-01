def main():
    n = int(input("Insira um valor para N: "))
    proximo = 1

    for i in range(1, n + 1):
        print(proximo)
        proximo += i + 1
        
main()
                  
