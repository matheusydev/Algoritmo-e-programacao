def main():
    B = int(input())
    T = int(input())

    area_nota = 160 * 70

    felix = (T + B) * 70 / 2

    if felix > area_nota/2:
         print(1)
    elif felix < area_nota/2:
        print(2)
    else:
        print(0)
main()