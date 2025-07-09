def main():
    while True:
        entrada = input().split()
        X = int(entrada[0])
        Y = int(entrada[1])

        if X == 0 or Y == 0:
            break
        elif X > 0 and Y > 0:
            print("primeiro")
        elif X < 0 and Y > 0:
            print("segundo")
        elif X < 0 and Y < 0:
            print("terceiro")
        else:  
            print("quarto")



main()