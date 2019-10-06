def counter(word, letter, start):
    count = 0
    aletter = start
    for aletter in word:
        if aletter == letter:
            count = count + 1
    print(count)

counter('ababac', 'a', 5)
