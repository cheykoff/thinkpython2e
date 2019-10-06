def has_duplicates(t):
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            if t[i] == t[j]:
                return True
    return False

t = [10, 20, 30, 40, 50]
print(has_duplicates(t))

'''
get list t
for all elements i of t from t[0] till t[n]
for all elements j of t from t[i+1] till t[n]
if i is equal j return True
if no two elements are found return False
'''
