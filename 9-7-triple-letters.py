def has_triple_letter(word):
    index = 0
    while index < len(word) - 2:
        if word[index] == word[index + 1] == word[index + 2]:
            return True
        index = index + 1
    return False

word = 'seee'
print(word, 'has triple letter', has_triple_letter(word))



