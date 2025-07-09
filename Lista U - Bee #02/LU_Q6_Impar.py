def main():
    x = int(input())
    i = 6

    while i > 0:
        if x % 2 != 0:
            print(x)
            i -= 1
        x += 1
main()