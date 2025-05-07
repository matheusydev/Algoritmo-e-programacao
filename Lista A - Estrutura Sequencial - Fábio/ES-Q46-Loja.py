print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-----------------------------------------")

# Entrada

valor = float(input("Insira o valor do produto: "))

# Processamento

parcela = valor // 3
entrada = (valor % 3) + parcela

# Saída

print(f"O valor de R$:{valor}, tem entrada de R$:{entrada:.2f} e 2 parcelas de R$:{parcela:.2f}")

