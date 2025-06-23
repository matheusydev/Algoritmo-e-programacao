def main():
    entrada = input().split()
    
    num1 = int(entrada[0])
    num2 = int(entrada[1])

    if num1 < num2 :
        tempo = num2 - num1
    else:
        tempo = num2 + 24 - num1
    
    print(f"O JOGO DUROU {tempo} HORA(S)")


main()