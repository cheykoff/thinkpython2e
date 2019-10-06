def print_long_words():
    fin = open('words.txt')
    count16 = 0
    count17 = 0
    count18 = 0
    count19 = 0
    count20 = 0
    count21 = 0
    count22andmore = 0
    for line in fin:
        if len(line) > 15:
            if len(line) > 21:
                count22andmore = count22andmore + 1
            elif len(line) == 21:
                count21 = count21 + 1
            elif len(line) == 20:
                count20 = count20 + 1
            elif len(line) == 19:
                count19 = count19 + 1
            elif len(line) == 18:
                count18 = count18 + 1
            elif len(line) == 17:
                count17 = count17 + 1
            elif len(line) == 16:
                count16 = count16 + 1
            print(line.strip())
    print(count22andmore, "words have 22 or more letters")
    print(count21, "words have 21 letters")
    print(count20, "words have 20 letters")
    print(count19, "words have 19 letters")
    print(count18, "words have 18 letters")
    print(count17, "words have 17 letters")
    print(count16, "words have 16 letters")
    
print_long_words()
