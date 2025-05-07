def main():
    n = int(input("n: "))
    
    somatorio = 0
    numerador = 1
    denominador = n
    
    while numerador <= n:
            somatorio = numerador / denominador
            numerador += 1
            denominador -= 1
            
    print(f"{somatorio:.8f}")
    
    
main()