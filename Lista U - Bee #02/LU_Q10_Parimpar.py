def main():
  N = int(input())

  while N > 0:
    num = int(input())

    if num % 2 == 0:
      classe = 'EVEN'
    else:
       classe = 'ODD'

    if num > 0:
      print(f'{classe} POSITIVE')
    elif num < 0:
      print(f'{classe} NEGATIVE') 
    else:
      print('NULL')

    N -= 1
main()