print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-----------------------------------------")

#Entrada

numero = int(input("insira o número de 3 digitos: "))

#Processamento

centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 100) % 10

#Saída  

print(f"o inverso de {numero} é: {unidade}{dezena}{centena}")
