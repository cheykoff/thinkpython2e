def is_sorted(t):
    s = sorted(t)
    if s == t:
        return True
    else: return False

t1 = ['a', 'c', 'r']
t2 = ['n', 'b', 'i']

print(is_sorted(t1))
print(is_sorted(t2))
