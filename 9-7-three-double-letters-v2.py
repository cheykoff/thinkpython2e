def count_words_with_triple_double_letters():
    fin = open('words.txt')
    count_words = 0
    for line in fin:
        index = 0
        word = line.strip()
        while index < len(word) - 5:
            if word[index] == word[index + 1] and word[index + 2] == word[index + 3] and word[index + 4] == word[index + 5] :
                count_words = count_words + 1
                print(word)
            index = index + 1
    print(count_words)


count_words_with_triple_double_letters()

