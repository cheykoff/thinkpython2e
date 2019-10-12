def create_dictionary():
	d = {}
	with open ('words.txt') as file:
		for line in file:
			word = line.strip().lower()
			d[word] = []
	return d

reducible_words = {}
reducible_words[''] = ['']

def get_children(d):
	d2 = {}
	for word in d:
		children = derive_children(word, d)
		d2[word] = children
	return d2

def derive_children(word, d):
	children = []
	i = 0
	for i in range(len(word)):
		child = word[:i] + word[i+1:]
		if child in d:
			children.append(child)
	return children

def filter_for_parents(d2):
	d3 = {}
	for word in d2:
		if word == '':
			d3[word] = d2[word]
		elif d2[word] != []:
			d3[word] = d2[word]
	return d3

def reduce(word, d):
	children = derive_children(word,d)
	for child in children:
		if child in reducible_words:
			reducible_words[word] = [child]
		else:
			reduce(child, d)

def print_trail(word, d):
	if word == '':
		print('!!!')
	else:
		print(word, end=' ')
		child = d[word]
		print_trail(child[0], d)

d = create_dictionary()
#print(d)

d2 = get_children(d)
#print(d2)

d3 = filter_for_parents(d2)
#print(d3)

for word in d3:
	reduce(word, d3)

#print(reducible_words)

max_length = 0
for word in reducible_words:
	max_length = max(max_length, len(word))

for word in reducible_words:
	if len(word) == max_length:
		print_trail(word, reducible_words)


