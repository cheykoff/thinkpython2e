def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

letters = 'aeiou'
word = 'uaeuweu'
if uses_only(word, letters):
    print('yes')
else:
    print('no')
