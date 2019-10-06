def nested_sum(t):
    result = 0
    for i in t:
        if type(i) == int:
            result += i
        else:
            result += nested_sum(i)
    return result

t = [[1, 2], [4, [2, 5]], 3]
print(nested_sum(t))
