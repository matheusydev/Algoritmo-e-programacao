def main():
    entrada = input().split()

    A = float(entrada[0])
    B = float(entrada[1])
    C = float(entrada[2])



    if (A < B + C and B < A + C and C < A + B):
        perimetro = A + B + C
        print(f"Perimetro = {perimetro:.1f}")
    else:
        area = ((A + B) / 2) * C
        print(f"Area = {area:.1f}")

main()
