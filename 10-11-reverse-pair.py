'''
Solution Approach
load word list and save words in a list
reverse all words and save in seperate list using bisect search 
compare words with bisect searc
'''

def create_word_list():
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word_list.append(line.strip())
    return word_list

def add_word_bisect(word, word_list):
    word = reverse_word(word)
    lo = 0
    hi = len(word_list)
    while lo < hi:
        mid = (lo+hi)//2
        if word < word_list[mid]:
            hi = mid
        else:
            lo = mid + 1
    word_list.insert(lo, word)
    return word_list

def create_rev_word_list(word_list):
    rev_word_list = []
    for word in word_list:
        rev_word_list = add_word_bisect(word, rev_word_list)
    return rev_word_list

def reverse_word(word):
    return word[::-1]

def compare_word_lists(word_list, rev_word_list):
    reversible_words = []
    for word in word_list:
        if in_bisect(word, rev_word_list):
            print(word)
    return None

def in_bisect(word, word_list):
    if len(word_list) == 0:
        return False
    i = len(word_list) // 2
    if word == word_list[i]:
        return True
    elif word < word_list[i]:
        return in_bisect(word, word_list[:i])
    elif word > word_list[i]:
        return in_bisect(word, word_list[i+1:])
    else:
        print('unknown error')

#print('word list:\n', create_word_list())

#print('\nreversed word list:\n', create_rev_word_list(create_word_list()))
compare_word_lists(create_word_list(), create_rev_word_list(create_word_list()))
