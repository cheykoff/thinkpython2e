def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

'''
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('value not in dictionary')
'''

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

h = histogram('the parrot is a lazy bird')

print(invert_dict(h))
