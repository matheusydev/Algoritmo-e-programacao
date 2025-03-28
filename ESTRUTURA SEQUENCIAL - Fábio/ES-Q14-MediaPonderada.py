print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-----------------------------------------")

# Entrada

nota1 = float(input("insira a nota 1: "))
peso1 = int(input("insira o peso da nota 1: "))
nota2 = float(input("insira a nota 2: "))
peso2 = int(input("insira o peso da nota 2: "))
nota3 = float(input("insira a nota 3: "))
peso3 = int(input("insira o peso da nota 3: "))

# Processamento

resultado = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3 ) / ( peso1 + peso2 + peso3)

# Saída

print(f"a média do aluno é {resultado:.2f}")