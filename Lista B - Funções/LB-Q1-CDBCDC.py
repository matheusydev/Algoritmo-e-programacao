# Entrada

investimento = float(input("insira o valor que sera investido: "))


def calcularCDB():
    taxaCDB = float(input("insira o valor da taxa do banco: "))
    tempoCDB = int(input("insira o tempo que sera investido (anos): "))
    jurosCompostoCDB = investimento * (1 + (taxaCDB / 100)) ** tempoCDB
    valorCDB = jurosCompostoCDB - investimento
    return valorCDB



def calcularCDC():
    taxaCDC = float(input("insira a taxa do CDC para cada mês: "))
    parcelaCDC = int(input("insira o total de parcelas para calcular o CDC: "))
    jurosCompostoCDC = investimento * (1 + (taxaCDC / 100)) ** parcelaCDC
    valorCDC = jurosCompostoCDC - investimento
    return valorCDC
    
 
#jurosComposto = calcularJurosComposto()    
valorCDB = calcularCDB()
print(f"CDB = {valorCDB:.2f}")
valorCDC = calcularCDC()
print(f"CDC  = {valorCDC:.2f}")