def cumsum(t):
    result = t[:]
    for i in range(1, len(result)):
        result[i] += result[i-1]
    return result

t = [10, 20, 30]
print(cumsum(t))
