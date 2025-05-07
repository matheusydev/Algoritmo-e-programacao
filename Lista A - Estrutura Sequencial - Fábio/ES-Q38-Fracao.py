print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-----------------------------------------")

# Entrada

numeprimeiro = int(input("Insira numerador da primeira fração: "))
denoprimeiro = int(input("Insira denominador da primeira fração: "))
numesegundo = int(input("Insira numerador da segunda fração: "))
denosegundo = int(input("Insira denominador da primeira fração: "))

# Processamento

numesoma = (numeprimeiro  * denosegundo)  + (numesegundo * denoprimeiro)
denosoma = denoprimeiro * denosegundo

# Saída

print(f"a soma da fração {numeprimeiro}/{denoprimeiro} + {numesegundo}/{denosegundo} = {numesoma}/{denosoma}")
