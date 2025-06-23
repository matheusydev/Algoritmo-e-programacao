def main():
    entrada = float(input())

    if entrada <= 2000:
        print("Isento")
    elif entrada <= 3000:
        total = entrada - 2000
        resultado = (total * 8) / 100
        print(f"R$ {resultado:.2f}")
    elif entrada <= 4500:
        total = entrada - 2000
        total1 = total - 1000
        taxa1 = (1000 * 8) / 100
        taxa2 = (total1 * 18) / 100
        resultado = taxa1 + taxa2
        print(f"R$ {resultado:.2f}")
    else:
        total = entrada - 2000
        total1 = total - 1000
        total2 = total1 - 1500
        taxa = (1000 * 8) / 100
        taxa1 = (1500 * 18) / 100
        taxa2 = (total2 * 28) / 100
        resultado = taxa + taxa1 + taxa2
        print(f"R$ {resultado:.2f}")

main()
