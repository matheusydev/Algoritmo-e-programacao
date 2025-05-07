def main():
    n = int(input("numero soma: "))
    numero = n
    resultado = 0
    
    while numero != 0:
        resultado += numero   
        numero = numero - 1
            
    print(f"{resultado}")    
    print("fim")
    
    
main()