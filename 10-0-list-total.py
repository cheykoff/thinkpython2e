def add_all(t):
    total = 0
    for i in range(len(t)):
        total = total + t[i]
    return total

t = [1, 2, 3]
print(add_all(t))
