def main():
    entrada = input().split()

    nota1 = float(entrada[0])
    nota2 = float(entrada[1])
    nota3 = float(entrada[2])
    nota4 = float(entrada[3])

    media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 4) + (nota4 * 1)) / 10

    print(f"Media: {media:.1f}")

    if media >= 7.0:
        print("Aluno aprovado.")
    elif media < 5.0:
        print("Aluno reprovado.")
    else:
        print("Aluno em exame.")
        nota_final = float(input())
        print(f"Nota do exame: {nota_final:.1f}")

        media_final = (media + nota_final) / 2

        if media_final >= 5.0:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        
        print(f"Media final: {media_final:.1f}")

main()
