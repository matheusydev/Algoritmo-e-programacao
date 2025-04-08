print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-----------------------------------------")

# Entrada

anosfuamndo = int(input("Insira quantos á quantos anos  o usuário fuma: "))
cigarrodia = int(input("Insira quantos cigarros fuma por dia: "))
precodocigarro = float(input("Insira o preço da cartela de cigarro: "))

# Processamento

totalcigarro = (anosfuamndo * 365) * cigarrodia
cartelas = totalcigarro / 20
gastototal = cartelas * precodocigarro

# Saída

print(f"O tatal de gasto com cigarro foi de R$:{gastototal:.2f}")