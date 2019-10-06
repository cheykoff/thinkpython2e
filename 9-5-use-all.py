def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True

def check_words_with_all_letters(letters):
    fin = open('words.txt')
    count = 0
    for line in fin:
        if uses_all(line, letters):
            print(line.strip())
            count = count + 1
    print(count) 

letters = 'acefhlo'
check_words_with_all_letters(letters)
