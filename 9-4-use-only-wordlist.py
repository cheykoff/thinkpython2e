def uses_only(word, letters):
    all_char_are_in_letters = True
    for char in word:
        char_is_in_letters = False
        for letter in letters:
            if char == letter:
                char_is_in_letters = True
        if not char_is_in_letters:
            all_char_are_in_letters = False
    return all_char_are_in_letters

def check_words_with_only_letters(letters):
    fin = open('words.txt')
    count = 0
    for line in fin:
        word = line.strip()
        if uses_only(word, letters):
            print(word)
            count = count + 1
    print(count)

letters = 'acefhlo'


check_words_with_only_letters(letters)
