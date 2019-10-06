def chop(t):
    del t[0]
    del t[len(t)-1]

t = [10, 20, 30, 40]

print(chop(t))
print(t)
