def avoids(palavra, letras_proibidas):
  for letra in palavra:
    if contem_caracter(letras_proibidas, letra):
      return False
  
  return True