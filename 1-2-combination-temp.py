'''
find all items in which at least 2 have 4 letters and 1 has 5 letters
'''

d = {'a': ['abcd', 'abce', 'abcde'], 'b': ['bbbb', 'bbbbb', 'ccccc']}

for item in d:
	print(item)
	print(d[item])
	for i in range(len(d[item])):
		print(d[item][i])
		print(len(d[item][i]))

print(d)