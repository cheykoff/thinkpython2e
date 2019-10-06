def counter(word, letter, start):
    index = start
    count = 0
    while index < len(word):
        if word[index] == letter:
            count = count + 1
        index = index + 1
    print(count)

counter('ababac', 'a', 2)
