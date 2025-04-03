print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-----------------------------------------")

# Entrada

numero = int(input("Entre com um número interiro de 3 digitos: "))

# Processamento

centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 100) % 10 

centenainverso = unidade * 100
dezenainverso = dezena * 10
unidadeinverso = centena * 1

inverso = centenainverso + dezenainverso + unidadeinverso

subtracao = numero - inverso

# Saída

print(f"{numero} - {inverso} = {subtracao}")
