def main():
    entrada = input().split()

    x = float(entrada[0])
    y = float(entrada[1])
    z = float(entrada[2])

    if x >= y and x >= z:
        A = x
        B = y
        C = z

    if y >= x and y >= z:
        A = y
        B = x
        C = z 
    
    if z >= x and z >= y:
        A = z
        B = x
        C = y

    if A >= B + C:
        print("NAO FORMA TRIANGULO")
    else:
        if A**2 == B**2 + C**2:
            print("TRIANGULO RETANGULO")
        elif A**2 > B**2 + C**2:
            print("TRIANGULO OBTUSANGULO")
        elif A**2 < B**2 + C**2: 
            print("TRIANGULO ACUTANGULO")

        if A == B and B == C:
            print("TRIANGULO EQUILATERO")
        elif A == B or B == C or A == C:
            print("TRIANGULO ISOSCELES")

main()
