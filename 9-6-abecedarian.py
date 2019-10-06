def is_abecedarian(word):
    word = word.lower()
    order_last = 0
    for letter in word:
        order = ord(letter)
        if not order > order_last:
            return False
        order_last = order
    return True

def check_words():
    fin = open('words.txt')
    count = 0
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            count = count + 1
    return count

print(check_words())
