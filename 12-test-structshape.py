from structshape import structshape
t = [1, 2, 3]
print(structshape(t))
t2 = [[1, 2, ['a', (1, 'b', {'a':1, ('a', 'b'): [1, 2,]})]], [3, 4, 'a'], (5, 6, 7)]

print(structshape(t2))