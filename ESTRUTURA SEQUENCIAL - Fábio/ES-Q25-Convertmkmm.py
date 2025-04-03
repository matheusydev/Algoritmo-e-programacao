print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-----------------------------------------")

# Entrada

distancia = float(input("Insira a distancia total em metros: "))

# Processamento

quilometros = distancia // 1000
metros = distancia % 1000

# Saída

print(f"{distancia}m = {quilometros}km e {metros}m")