def sort_words(word1, word2):
    word1_lower = word1.lower()
    word2_lower = word2.lower()
    if word1_lower < word2_lower:
        print(word1, 'comes before', word2)
    elif word1_lower > word2_lower:
        print(word1, 'comes after', word2)
    else:
        print(word1, 'is the same as', word2)

sort_words('Lanna', 'anna')
