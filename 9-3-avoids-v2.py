def open_word_list():
    return open('words.txt')

def get_forbidden_letters():
    return input('Enter the forbidden letters as a string:')

def avoids(word, forbidden_letters):
    for char in word:
        for letter in forbidden_letters:
            if char == letter:
                return False
    return True

def check_word_list_for_forbidden_letters():
    count = 0
    forbidden_letters = get_forbidden_letters()
    for line in open_word_list():
        if avoids(line, forbidden_letters):
            count = count + 1
    print('Number of words w/o forbidden letters', forbidden_letters, 'is:', count)

check_word_list_for_forbidden_letters()
