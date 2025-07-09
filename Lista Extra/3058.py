def main():
    N = int(input())

    menor_preco_por_kg = float('inf')

    for _ in range(N):
        line_input = input()
        parts = line_input.split()
        P = float(parts[0])
        G = float(parts[1])
        preco_atual_por_kg = (P / G) * 1000
        if preco_atual_por_kg < menor_preco_por_kg:
            menor_preco_por_kg = preco_atual_por_kg

    print(f"{menor_preco_por_kg:.2f}")
main()