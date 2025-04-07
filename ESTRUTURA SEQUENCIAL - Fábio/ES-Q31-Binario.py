print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-----------------------------------------")

# Entrada

numero = int(input("Entre com um número em binario com 4 digitos: "))

# Processamento

unidademilhar = numero // 1000
centena = (numero % 1000) // 100
dezena = ((numero % 100) % 100) // 10
unidade = (((numero % 100) % 100) % 10) % 10

primeiro = unidademilhar * 2 ** 3
segundo = centena * 2 ** 2
terceiro = dezena * 2 ** 1
quarto = unidade * 2 ** 0

resultado = primeiro + segundo + terceiro + quarto

# Saída

print(f"{numero} em binario é {resultado} em decimal")
