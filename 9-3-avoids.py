def avoids(word, forbidden_letters):
    for char in word:
        for forbidden_letter in forbidden_letters:
            if char == forbidden_letter:
                return False
    return True

word = 'hello'
forbidden_letters = 'ir'

if avoids(word, forbidden_letters):
    print('no forbidden letters:', forbidden_letters, 'in the word:', word)
else:
    print('there is at least one of these forbidden letters:', forbidden_letters, 'in the word:', word)
    
