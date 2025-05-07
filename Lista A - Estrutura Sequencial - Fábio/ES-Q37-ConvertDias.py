print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-----------------------------------------")

# Entrada

total = int(input("Insira quantos dias de vida você tem: "))

# Processamento

anos = total // 365
meses = (total % 365) // 30
dias = (total % 365) % 30

# Saída

print(f"Com o total de {total} dias você tem {anos} anos, {meses} meses e {dias} dias")