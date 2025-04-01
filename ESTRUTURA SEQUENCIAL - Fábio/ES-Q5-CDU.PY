print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-----------------------------------------")

# Entrada

numero = int(input("Entre com um numero interiro de 3 digitos: "))

# Processamento

centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 100) % 10 

# Saída

print(f"{numero} --> ({centena})centena, ({dezena})dezena e ({unidade})unidade")
