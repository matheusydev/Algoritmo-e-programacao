def main():
    num1 = int(input())
    num2 = int(input())

    soma = 0

    if num1 > num2:
        num1 -= 1
        while num1 > num2:
            if num1 % 2 != 0:
                soma += num1
            num1 -= 1

    if num2 > num1:
        num2 -= 1
        while num2 > num1:
            if num2 % 2 != 0:
                soma += num2
            num2 -= 1

  
    print(f"{soma}")


main()