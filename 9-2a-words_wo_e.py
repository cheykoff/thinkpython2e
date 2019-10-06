def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

def print_words_wo_e():
    fin = open('words.txt')
    count_words = 0
    count_words_wo_e = 0
    for line in fin:
        count_words = count_words + 1
        if has_no_e(line):
            count_words_wo_e = count_words_wo_e + 1
    print('words:', count_words)
    print("words w/o 'e':", count_words_wo_e)
    print("percentag of words w/o 'e':", count_words_wo_e/count_words*100, '%')


print_words_wo_e()
