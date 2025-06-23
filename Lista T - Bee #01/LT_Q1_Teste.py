def main():
    entrada = input()

    a = int(entrada.split()[0])
    b = int(entrada.split()[1])
    c = int(entrada.split()[2])
    d = int(entrada.split()[3])
    
        
    if (b > c) and (d > a) and (c + d > a + b) and (c > 0) and (d > 0) and (a % 2 == 0):
        print("Valores aceitos")
    else:
        print("Valores nao aceitos")
        
main