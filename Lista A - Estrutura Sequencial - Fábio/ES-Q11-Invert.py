print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-----------------------------------------")

# Entrada

num = int(input("Entre com um numero interiro de 3 digitos: "))

# Processamento

centena = num // 100
dezena = (num % 100) // 10
unidade = (num % 100) % 10 


# Saída

print(f"{unidade}{dezena}{centena}")

