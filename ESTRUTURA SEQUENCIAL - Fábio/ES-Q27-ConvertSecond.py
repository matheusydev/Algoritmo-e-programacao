print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-----------------------------------------")

# Entrada

total = int(input("Insira o valor total de segundos: "))

# Processamento

horas = total // 3600
minutos = (total % 3600) // 60
segundos = (total % 3600) % 60

# Saída

print(f"{total}segundos = {horas}h {minutos}min e {segundos}s")
