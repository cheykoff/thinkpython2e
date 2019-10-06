def is_reverse(word1, word2):
    if len(word1) != len(word2):
        print('Length does not match')
    else:
        index = 0
        while index < len(word1):
            if word1[index] == word2[-1 - index]:
                index = index + 1
            else:
                print(word1, 'is NOT the same as', word2, 'backwards')
                return
        print(word1, 'is the same as', word2, 'backwards')

is_reverse('abc', 'cba')
        
