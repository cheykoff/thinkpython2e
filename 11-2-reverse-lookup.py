def invert_dict(d):
	inverse = {}
	for key in d:
		val = d[key]
		inverse.setdefault(val, []).append(key)
		print(key, d[key])
		'''
		if val in inverse:
			inverse[val].append(key)
		else:
			inverse[val] = [key]
		'''
	return inverse

d = {'one': 'uno', 'two': 'dos', 'three': 'uno'}
print(d)
print(invert_dict(d))