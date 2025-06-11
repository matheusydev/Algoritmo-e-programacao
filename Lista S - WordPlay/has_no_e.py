def main():
    while True:
        menu_word() 
        choose = int(input('Choose a option: '))
        if choose == 1: 
            has_no_letter()
        elif choose == 2:
            size_word()
        elif choose == 3: 
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


def menu_word():
    interface = '''
>>> Words Play <<< 
1 - If you want to choose a letter
2 - If you want to choose the size of the word
3 - Exit
'''
    print(interface)

main()