def find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

word = 'awesome'
letter = 'e'
start = 3
print(find(word, letter, start))
