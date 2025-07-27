def main():

    nomes_validos = []
    nome = None
    while nome != "fim":
        nome = input('Digite seu nome ou "fim" para encerrar: ').strip()

        nome_sem_espaco = nome.replace(" ", "")

        if len(nome_sem_espaco) >= 4:
            nomes_validos.append(nome_sem_espaco)
    
    print(f"Quantidade de nomes válidos: {len(nomes_validos)}")




main()