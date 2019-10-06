def uses_only(word, letters):
    all_char_are_in_letters = True
    for char in word:
        char_is_in_letters = False
        for letter in letters:
            if char == letter:
                char_is_in_letters = True
        if not char_is_in_letters:
            all_char_are_in_letters = False
    return all_char_are_in_letters

letters = 'aeiou'
word = 'uaeueu'
if uses_only(word, letters):
    print('yes')
else:
    print('no')
