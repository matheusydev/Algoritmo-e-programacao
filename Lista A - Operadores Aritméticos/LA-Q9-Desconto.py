print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-----------------------------------------")

#Entrada 

preco = int(input("insira o preço: "))
desconto = int(input("insira o desconto: "))

#Processamento 

resultado = preco - (preco * (desconto / 100))

#Sada

print(f"o valor final do produto é: {resultado}")
