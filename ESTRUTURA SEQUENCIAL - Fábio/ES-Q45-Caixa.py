print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-----------------------------------------")

# Entrada

saque = int(input("Insira quanto você quer sacar: "))

# Processamento

cinquenta = saque // 50
dez = (saque % 50) // 10
cinco = ((saque % 50) % 10) // 5
um = ((saque % 50) % 10) % 5

# Saída

print(f"o valor de R$:{saque} você vai receber {cinquenta} notas de cinquenta, {dez} notas de dez, {cinco} notas de cinco e {um} notas de um real")


