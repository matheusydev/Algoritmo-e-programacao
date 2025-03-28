print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-----------------------------------------")

#Entrada

capital = float(input("insira o capital: "))
taxa = float(input("insira a taxa: "))
tempo = int(input("insira o tempo: "))

#Processamento

juros = (capital * taxa * tempo) / 100
jurossimples = capital * juros

#Saida

print(f"o juros simples é de: {jurossimples:.2f}")