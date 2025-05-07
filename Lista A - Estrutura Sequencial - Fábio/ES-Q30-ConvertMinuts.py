print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-----------------------------------------")

# Entrada

total = int(input("Insira o valor total de minutos: "))

# Processamento

dias = total // 1440
horas = (total % 1440) // 60
minutos = (total % 3600) % 60

# Saída

print(f"{total} minutos = {dias} dias, {horas} horas, {minutos} minutos")

