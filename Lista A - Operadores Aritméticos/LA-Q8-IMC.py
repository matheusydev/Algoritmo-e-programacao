print(">>>>>>>>>>     Matheusydev     <<<<<<<<<<")
print("-----------------------------------------")

#Entrada

peso = int(input("insira o seu peso: "))
altura = float(input("insira a sua altura: "))


#Processamento

imc = peso / (altura ** 2) # pode se usar um if para verificar o estado da pessoa

#Saida  
print(f'seu IMC é {imc:.2f}') 
