from io_utils import obter_numero_inteiro

def main():
  
  ano = obter_numero_inteiro("Ano: ")

  if confere_ano_bissexto(ano):
    print(f' O ano de {ano} é bissexto')
  else:
    print(f"O ano de {ano} não é bissexto")


def confere_ano_bissexto(ano: int):
  return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0

main()