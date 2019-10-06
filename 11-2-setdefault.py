d = {'one': 'uno', 'two': 'duo'}
d_inverted = {}
d_inverted2 = dict()
print('d', ' is a ', type(d))
print('d_inverted', d_inverted, ' is a ', type(d_inverted))
print('d_inverted2', d_inverted2, ' is a ', type(d_inverted2))



for key in d:
	val = d[key]
	print(val)
	if val in d_inverted:
		d_inverted[val].append()
print(d.setdefault('three', 'default'))

print(d)