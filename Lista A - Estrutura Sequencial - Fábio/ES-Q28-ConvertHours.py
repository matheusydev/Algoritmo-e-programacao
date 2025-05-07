print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-----------------------------------------")

# Entrada

total = int(input("Insira o valor total de horas: "))

# Processamento

semana = total // 168
dias = (total % 168) // 24
horas = (total % 168) % 24

# Saída

print(f"{total}horas = {semana}semanas, {dias}dias e {horas}horas")