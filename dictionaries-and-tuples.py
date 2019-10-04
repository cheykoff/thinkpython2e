d = {'a': 0, 'b': 1, 'c': 2}
t = d.items()
print(t)

for key, value in t:
	print(key, value)

t2 = [('a', 0), ('b', 1), ('c', 2)]
d = dict(t2)
print(d)

d = dict(zip('abc', range(3)))
print(d)

d.update([('d', 3), ('e', 4)])
print(d)

first = 'Sean'
last = 'Connery'
number = '089'
directory = {}
directory[last, first] = number

for last, first in directory:
	print(last, first, number)
'''
t3 = list((1, 5, 3))
t4 = tuple(sorted(t3))
t5 = reversed(t3)
t6 = reversed(t4)
'''
#7 = tuple(list((1, 3, 7, 5, 2)).sort())
l = [1, 3, 2]
print(l)
l.sort()
print(l)
#print(t7)
"""
print(t3)
print(t4)
print(t5)
print(t6)
"""