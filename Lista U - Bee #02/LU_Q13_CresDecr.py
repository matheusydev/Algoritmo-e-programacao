def main():
    while True:
        entrada = input().split()
        
        x = int(entrada[0])
        y = int(entrada[1])

        if x == y:
            break
        elif x < y:
            print("Crescente")
        elif x > y:
            print("Decrescente")
main()