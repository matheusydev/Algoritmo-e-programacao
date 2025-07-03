def main():
    N = int(input())

    for _ in range(N):
        entrada = input().split()
        num1 = float(entrada[0])
        num2 = float(entrada[1])
        num3 = float(entrada[2])

        nota1 = num1 * 2
        nota2 = num2 * 3
        nota3 = num3 * 5

        media = (nota1 + nota2 + nota3) / 10

        print(f"{media:.1f}")
main()