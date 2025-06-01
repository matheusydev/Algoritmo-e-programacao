def main():
    n = int(input("Insira um valor para somar com os anteriores: "))
    somatorio = n 

    for i in range(1, n):
        anterior = n - 1
        somatorio += anterior 
        n -= 1

    print(somatorio)
          
main()
            