def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def print_hist(h):
    for key in h:
        print (key, h[key])

def print_hist_sorted(h):
    for key in sorted(h):
        print (key, h[key])

h = histogram("parrot")

print_hist(h)
print_hist_sorted(h)
