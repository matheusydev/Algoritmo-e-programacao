print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-----------------------------------------")

# Entrada

x1 = int(input("Insira o valor de x1: "))
x2 = int(input("Insira o valor de x2: "))
y1 = int(input("Insira o valor de y1: "))
y2 = int(input("Insira o valor de y2: "))

# Processamento

distancia = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

# Saída

print(f"a distancia é {distancia:.2f}")


