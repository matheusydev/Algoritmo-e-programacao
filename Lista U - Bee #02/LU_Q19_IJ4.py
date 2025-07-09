def main():
    I = 0.0
    J = 1.0
    aux = 0.2

    for _ in range(11):
        for _ in range(3):
            if I == 0.0:
                print(f"I={int(I)} J={int(J)}")
            elif I == 1.0:
                print(f"I={int(I)} J={int(J)}")
            elif I > 1.9 and I < 2.1:
                print(f"I={2} J={int(J)}")
            else:
                print(f"I={I:.1f} J={J:.1f}")

            J += 1
        J = 1.0 + aux
        I += 0.2
        aux += 0.2


main()