def main():
    N = int(input())
    i = 1
    while i < N + 1:
        x = i
        y = i * i
        z = x * y
        print(f"{x} {y} {z}" )

        print(f"{x} {y+1} {z+1}")
        i += 1

main()