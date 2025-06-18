import utils
def main():
    while True:
        menu_word() 
        choose = int(input('Choose a option: '))
        if choose == 1: 
            has_no_letter()
        elif choose == 2:
            size_word()
        elif choose == 3:
            avoids_letters()
        # elif choose == 4:
        #     size_word()
        # elif choose == 5:
        #     size_word()
        # elif choose == 6:
        #     size_word()
        elif choose == 0: 
            break

def has_no_letter():
    letters = str(input('Choose any letter: '))
    words = open('words.txt')
    all = 0
    find = 0

    for letter in words:
        all += 1
        if not letters in letter:
            word = letter.strip()
            print(word)
            find +=1
    print(f'The percentage of words that has no letter "{letters}" is: {(find/all)*100:.1f}% ')

def size_word():
    size = int(input('What size do you want?: '))
    words = open('words.txt')
    all = 0
    find = 0

    for letter in words:
        all += 1
        if size <= len(letter):
            word = letter.strip()
            print(word)
            find +=1
    print(f'The percentage of words greater than "{size}" is: {(find/all)*100:.1f}% ')

def avoids_letters():
    words = open('words.txt')
    forbideen = input('insert the forbidden letters: ')

    for letter in words:
    word = letter.strip()
    if utils.avoids(word, forbideen):
      print(words)

def show_words_with_allowed_letters():
  sin = open("br-sem-acentos.txt")

def menu_word():
    interface = '''
>>> Words Play <<< 
1 - If you want to choose a letter (9.1)
2 - If you want to choose the size of the word (9.2)
3 - Words without forbidden letters (9.3)
4 - Words with allowed letters onl (9.4)
5 - Words with mandatory letters (9.5)
6 - Words with letters in alphabetical order (9.6)

0 - Exit
'''
    print(interface)

main()