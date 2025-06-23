def main():
    subfilo = input()
    classe = input()
    alimentacao = input()

    if subfilo == "vertebrado":
        if classe == "ave":
            if alimentacao == "carnivoro":
                print("aguia")
            else:
                print("pomba")
        elif classe == "mamifero":
            if alimentacao == "onivoro":
                print("homem")
            else:
                print("vaca")
    elif subfilo =="invertebrado":
        if classe == "inseto":
            if alimentacao == "hematofago":
                print("pulga")
            else:
                print("lagarta")
        elif classe == "anelideo":
            if alimentacao == "hematofago":
                print("sanguessuga")
            else:
                print("minhoca")

main()