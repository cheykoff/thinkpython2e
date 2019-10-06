def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('value not in dictionary')


def invert_dict(d):
    v = 1
    v_max = 0
    for k in d:
        v_max = max(v_max, d[k])
    print(v_max)
    while v <= v_max:
        print(v, reverse_lookup(d,v))
        v += 1



h = histogram('parrot')
print(reverse_lookup(h, 2))

invert_dict(h)
