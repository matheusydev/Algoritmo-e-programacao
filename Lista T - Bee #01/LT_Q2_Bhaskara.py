def main():
    
    entrada = input().split()

    num1 = float(entrada[0])
    num2 = float(entrada[1])
    num3 = float(entrada[2])

    delta = (num2** 2)-4*num1*num3

    if delta < 0 or num1 == 0:
        print("Impossivel calcular")
    elif delta == 0:
        resultado1 = (-num2 + delta** 0.5)/(2 * num1)
        resultado2 = resultado1
        print(f"R1 = {resultado1:.5f}")
        print(f"R2 = {resultado2:.5f}")
    else:
        resultado1 = (-num2 + delta** 0.5)/(2*num1)
        resultado2 = (-num2 - delta** 0.5)/(2*num1)
        print(f"R1 = {resultado1:.5f}")
        print(f"R2 = {resultado2:.5f}")

main()
