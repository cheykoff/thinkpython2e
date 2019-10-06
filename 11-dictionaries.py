def histogram(s):
	d = dict()
	for c in s:
		d.get(c, 1)
	return d

h = histogram('abca')
print(h)


