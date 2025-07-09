def main():

    M = int(input())
    A = int(input())
    B = int(input())

    X = M - A - B

    if X > A and X > B:
        print(X)
    elif A > B and A > X:
        print(A)
    else:
        print(B)

main()