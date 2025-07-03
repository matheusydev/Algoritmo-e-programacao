def main():
    N = int(input())
    dentro = 0
    fora = 0
    for _ in range(N):
        num = int(input())
        if num >= 10 and num <= 20:
            dentro += 1
        else:
            fora += 1
    
    print(f"{dentro} in")
    print(f"{fora} out")


main()