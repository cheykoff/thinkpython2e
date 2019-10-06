d = {'a':0, 'b':1, 'c':2, 'd': 3, 'e': 4}
t = d.items()
print(t)

for key, value in d.items():
	print(key, value)

t = [('a', 0), ('c', 2), ('b', 1)]
d = dict(t)
print(d) 

d = dict(zip('abc', range(3)))
print(d)

d.update([('d', 3),('e', 4)])
print(d)

last = 'mattes'
first = 'anna'
number = 1234
directory = {}
directory[last, first] = number

print(directory)

for last, first in directory:
	print(first, last, directory[last, first])

t = 'a', 'b', 'anna'
print(reversed(t))
