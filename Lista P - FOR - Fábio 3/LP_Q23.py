def main():

    funci = int(input("Insira a quantidade de funcionairos: "))

    for i in range(1, funci + 1):
        print(f"------------ FUNCIONARIO {i} ------------")
        hora = int(input("Insira a quantidade de horas trabalhada: "))
        dependentes = int(input("Insira a quantidade de dependentes: "))

        salario = (hora * 12) + (dependentes * 40)
        inss = salario * (8.5 / 100)
        ir = salario * (5 / 100)

        final = salario - (inss + ir)

        print(f"""========= RESULTADO =========
        horas trabalhada: {hora}
        dependentes: {dependentes}
        salario: R$: {salario}
        INSS: R$ {inss}
        IR: R$ {ir}
        Valor Final: R$: {final}
        """)
        #limpar a tela

main()


