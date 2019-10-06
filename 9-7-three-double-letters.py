def count_words_with_double_letters():
    fin = open('words.txt')
    count_words = 0
    for line in fin:
        index = 0
        count_double_letters = 0
        word = line.strip()
        while index < len(word) - 1:
            if word[index] == word[index + 1]:
                count_double_letters = count_double_letters + 1
                count_words = count_words + 1
                if count_double_letters >= 3:
                    print(word, count_double_letters)
            index = index + 1
    print(count_words)


count_words_with_double_letters()

check each letter, if same as letter before

