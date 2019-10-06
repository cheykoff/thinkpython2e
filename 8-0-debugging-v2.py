def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        index = 0
        while index < len(word1):
            if word1[index] == word2[-1 - index]:
                index = index + 1
            else:
                return False
        return True

word1 = 'abc'
word2 = 'cba'

if is_reverse(word1, word2):
    print("'" + word1 + "' is the same as '" + word2 +"' backwards")
else:
    print("'" + word1 + "' is the NOT same as '" + word2 +"' backwards")



