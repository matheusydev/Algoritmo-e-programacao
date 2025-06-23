def main():
    entrada = input().split()
    
    lanche = int(entrada[0])
    quntidade = int(entrada[1])

    if lanche == 1:
        preco = 4 * quntidade
    elif lanche == 2:
        preco = 4.5 * quntidade
    elif lanche == 3:
        preco = 5 * quntidade
    elif lanche == 4:
        preco = 2 * quntidade
    elif lanche == 5:
        preco = 1.5 * quntidade

    print(f"Total: R$ {preco:.2f}")

main()
