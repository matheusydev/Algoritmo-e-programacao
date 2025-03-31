# Entrada

    #CDB valor final = investimento *(1+ taxa de juros)^tempo

investimentoCDB = float(input("insira o valor que sera investido no CDB: "))
taxa = float(input("insira o valor taxa do banco: "))
tempo = float(input("insira o tempo investido: "))

    #CDC valor final = investimento * (taxa de jurus (1 + taxa de juros )^n ) // ((1 + taxa de juros)^n - 1)

# Processamento 
valorfinal = investimentoCDB * (1 + taxa) ** tempo 


#Saída 

print(f"{valorfinal}")