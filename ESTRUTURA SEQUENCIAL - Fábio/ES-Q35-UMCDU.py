print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-----------------------------------------")

# Entrada

numero = int(input("Entre com um número interiro de 4 digitos: "))

# Processamento

unidademilhar = numero // 1000
centena = (numero % 1000) // 100
dezena = ((numero % 100) % 100) // 10
unidade = (((numero % 100) % 100) % 10) % 10

soma = unidademilhar + centena + dezena + unidade
# Saída

print(f"({numero}) -> {unidademilhar} + {centena} + {dezena} + {unidade} = {soma}")
