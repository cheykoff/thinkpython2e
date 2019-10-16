def create_dictionary():
	d = {}
	with open ('words.txt') as file:
		for line in file:
			word = line.strip().lower()
			d[word] = []
	return d

def get_children(d):
	for word in d:
		children = derive_children(word, d)
		d[word] = children
	return d

def derive_children(word, d):
	children = []
	i = 0
	for i in range(len(word)):
		child = word[:i] + word[i+1:]
		if child in d:
			children.append(child)
	return children

def reduce(word, d):
	if word in reducible_words:
		return reducible_words[word]
	children = derive_children(word,d)
	reducible_child = []
	for child in children:
		if reduce(child, d):
			reducible_child.append(child)
			reducible_words[word] = reducible_child
			return reducible_child

def print_trail(word, d):
	if word == '':
		print('!!!')
	else:
		print(word, end=' ')
		child = d[word]
		print_trail(child[0], d)

d = get_children(create_dictionary())

reducible_words = {}
reducible_words[''] = ['']

for word in d:
	reduce(word, d)

max_length = 0
for word in reducible_words:
	if reducible_words[word] != []:
		max_length = max(max_length, len(word))

for word in reducible_words:
	if len(word) == max_length:
		if reducible_words[word] != []:
			print_trail(word, reducible_words)


