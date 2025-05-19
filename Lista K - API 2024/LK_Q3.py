import utils
import os
def main():


    soma_nota = 0
    soma_nota_masc = 0
    soma_nota_femi = 0
    qtd_masc = 0
    qtd_femi = 0
    maior_nota = 0
    menor_nota = 11
    

    while True:
        utils.clear()
        sexo = utils.obter_string("Entre com M ou F: ")
        if sexo.upper() == 'M':
            qtd_masc += 1
            nota = utils.obter_numero_real_q3("Nota do Aluno: ")
            soma_nota += nota
            soma_nota_masc += nota
            if nota > maior_nota:
                    maior_nota = nota
            if nota < menor_nota:
                    menor_nota = nota
        elif sexo.upper() == 'F':
            qtd_femi += 1
            nota = utils.obter_numero_real_q3("Nota do Aluna: ")
            soma_nota += nota
            soma_nota_femi += nota
            if nota > maior_nota:
                    maior_nota = nota
            if nota < menor_nota:
                    menor_nota = nota
        else:
            break

    
    media_geral = soma_nota / (qtd_masc + qtd_femi)
    media_masc = soma_nota_masc / qtd_masc
    media_femi = soma_nota_femi / qtd_femi
    perf_masc = (soma_nota_masc / soma_nota) * 100
    perf_femi = (soma_nota_femi / soma_nota) * 100
    desp_geral = media_geral / (qtd_masc + qtd_femi)
    result_desp_geral = calc_desempenho_geral(media_geral)
    desp_masc = soma_nota_masc / qtd_masc
    result_desp_masc = calc_desempenho_masc(media_masc)
    desp_femi = soma_nota_femi / qtd_femi
    result_desp_femi = calc_desempenho_femi(media_femi)

    utils.clear()
    print(f"""--------------- NOTAS DO ALUNOS ---------------

MÉDIA = {media_geral:.2f}
MAIOR NOTA = {maior_nota:.2f}
MENOR NOTA = {menor_nota:.2f}
PERFORMACE MASCULINA = {perf_masc:.2f}%
PERFORMACE FEMININA = {perf_femi:.2f}%
DESEMPENHO GERAL = {result_desp_geral}
DESEMPENHO GERAL = {result_desp_masc}
DESEMPENHO GERAL = {result_desp_femi}

""")
    
def calc_desempenho_geral(media_geral):
    if media_geral <= 2:
        return 'PÉSSIMO'
    elif media_geral <= 4:
        return 'RUIM'
    elif media_geral < 7:
        return 'REGULAR'
    elif media_geral < 8:
        return 'BOM'
    elif media_geral <= 10:
        return 'EXECELENTE'

def calc_desempenho_masc(media_masc):
    if media_masc <= 2:
        return 'PÉSSIMO'
    elif media_masc <= 4:
        return 'RUIM'
    elif media_masc < 7:
        return 'REGULAR'
    elif media_masc < 8:
        return 'BOM'
    elif media_masc <= 10:
        return 'EXECELENTE'
    
def calc_desempenho_femi(media_femi):
    if media_femi <= 2:
        return 'PÉSSIMO'
    elif media_femi <= 4:
        return 'RUIM'
    elif media_femi < 7:
        return 'REGULAR'
    elif media_femi < 8:
        return 'BOM'
    elif media_femi <= 10:
        return 'EXECELENTE'


main()