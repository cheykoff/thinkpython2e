def store_words_in_list_a():
    fin = open('words-short.txt')
    t = []
    for line in fin:
        t = t + [line.strip()]
    return t

def store_words_in_list_b():
    fin = open('words.txt')
    t = []
    for line in fin:
        t.append(line.strip())
    return t

print(store_words_in_list_a())
