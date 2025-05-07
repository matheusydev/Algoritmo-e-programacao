distanciafinal = None

def calculardistanciafinal():  
  global distanciafinal
  distancia = float(input("Insira a distancia total da viagem: "))
  bateria = float(input("Qual a porcetagem do percurso consegue ser feito com as baterias?: "))
  distanciafinal = distancia - (distancia * (bateria / 100))

def calculargasolina():
  global distanciafinal
  precogasolina = float(input("fale o preço da gasolina; "))
  aproveitamentogas = float(input("Quanto consegue km consegue rodas com 1L gasolina: "))
  distanciagas = distanciafinal / aproveitamentogas
  gastogasolina = distanciagas * precogasolina
  print(f"O gasto de gasolina é de: R${gastogasolina:.2f}") 
  

def calcularalcool():
  global distanciafinal
  precoalcool = float(input("fale o preço do alcool: "))
  aproveitamentoalc = float(input("Quanto consegue km consegue rodas com 1L alcool: "))
  distancialc = distanciafinal / aproveitamentoalc
  gastoalcool = distancialc * precoalcool
  print(f"O gasto de alcool é de: R${gastoalcool:.2f}") 


calculardistanciafinal()
calculargasolina()
calcularalcool()