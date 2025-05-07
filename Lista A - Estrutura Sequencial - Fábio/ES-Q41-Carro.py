print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-----------------------------------------")

# Entrada

valorfabrica = float(input("Insira o valor gasto para produzir o carro: "))
pordistribuidor = float(input("Insira a porcentagem do distribuidor: "))
porimposto = float(input("Insira a porcentagem de impsto: "))

# Processamento

valorDistribuidor = (valorfabrica / 100) * pordistribuidor
valorImposto = (valorfabrica / 100) * porimposto
precofinal = valorfabrica + valorDistribuidor + valorImposto

# Saída

print(f"o preço final do carro é de R$:{precofinal:.2f}")
