import q1_number_utils
import utils
def main():
    total = 0
    backend = 0
    frontend = 0
    mobile = 0
    dados = 0

    utils.clear()
    ctrl = q1_number_utils.obter_numero_inteiro("Insira a quantidade de entrevista: ")

    while ctrl > 0:
        entrada = input("Insira a quantidade de aluno e área: ")
        aluno = int(entrada.split()[0])
        tipo = (entrada.split()[1].upper())

        total += aluno 
        ctrl -= 1

        if tipo == "B":
            backend += aluno
        elif tipo == "F":
            frontend += aluno     
        elif tipo == "M":
            mobile += aluno       
        else:
            dados += aluno


    percetual_backend = (backend / total) * 100         
    percetual_frontend = (frontend / total) * 100         
    percetual_mobile = (mobile / total) * 100         
    percetual_dados = (dados / total) * 100

    utils.clear()
    print(f"""------------------------ RESULTADOS ------------------------
    Total: {total} alunos
    Total de backend: {backend}
    Total de frontend: {frontend}
    Total de moblie: {mobile}
    Total de dados: {dados}
    precetual de backend: {percetual_backend:.2f}%
    precetual de frontend: {percetual_frontend:.2f}%
    precetual de mobile: {percetual_mobile:.2f}%
    precetual de dados: {percetual_dados:.2f}%
    """)         
            




main()