print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-------------média ponderada-------------")

#Entrada 
nota1 = int(input("insira a nota 1: "))
peso1 = int(input("insira o peso da nota 1: "))
nota2 = int(input("insira a nota 2: "))
peso2 = int(input("insira o peso da nota 2: "))
nota3 = int(input("insira a nota 3: "))
peso3 = int(input("insira o peso da nota 3: "))

#Processamento
media1 = nota1 * peso1
media2 = nota2 * peso2
media3 = nota3 * peso3

mediaponderada = (media1 + media2 + media3) / (peso1 + peso2 + peso3) 

#Saida
print(f"a média ponderada é: {mediaponderada}")
