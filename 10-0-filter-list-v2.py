def filter_list(t):
    new_list = []
    for x in t:
        if x.isupper():
            new_list.append(x)
    return new_list

t = ['a', 'B', 'c', 'D']
print(t)
print(filter_list(t))
