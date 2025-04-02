print(">>>>>> Matheusydev <<<<<<<")
print("==========================")

# Entrada
print("\n--------------------------")
print("Calculadora de CDI e CDB")
print("--------------------------\n")
investimento = float(input("Insira o valor que sera investido: "))


#Função para calcular o CDB
def calcularCDB():
    taxaCDB = float(input("insira o valor da taxa do banco: "))
    tempoCDB = int(input("insira o tempo que sera investido (anos): "))
    jurosCompostoCDB = investimento * (1 + (taxaCDB / 100)) ** tempoCDB
    valorCDB = jurosCompostoCDB - investimento
    return valorCDB


#Função para calcular o CDC
def calcularCDC():
    taxaCDC = float(input("insira a taxa do CDC para cada mês: "))
    parcelaCDC = int(input("insira o total de parcelas para calcular o CDC: "))
    jurosCompostoCDC = investimento * (1 + (taxaCDC / 100)) ** parcelaCDC
    valorCDC = jurosCompostoCDC - investimento
    return valorCDC
    
 
# Saída
print("\n\n========== CALCULAR O CDB ==========")
valorCDB = calcularCDB()
print(f"CDB = {valorCDB:.2f}")
print("\n\n========== CALCULAR O CDC ==========")
valorCDC = calcularCDC()
print(f"CDC  = {valorCDC:.2f}")