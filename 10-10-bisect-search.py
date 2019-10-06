def in_bisect(s, t):
    low = 0
    high = len(t)
    mid = (len(t)//2)
    if len(t) == 0:
        return False
    elif t[mid] == s:
        return True
    elif t[mid] < s:
        low = mid
    elif t[mid] > s:
        high = mid
    else:
        print('unexpected result')
    return in_bisect(s, t[low:high])
    
def store_words_in_list():
    fin = open('words-short.txt')
    t = []
    for line in fin:
        t.append(line.strip())
    return t

s = 'zoo'
t = store_words_in_list()
print(s)
print(in_bisect(s, t, ))


