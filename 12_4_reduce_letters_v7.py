def create_dictionary():
	d = {}
	with open ('words-test.txt') as file:
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
	print('reduce word:', word)
	if word in reducible_words:
		print('is in reducible words', word, reducible_words[word])
		return reducible_words[word]
	print('is not yet in reducible_words')
	reducible_children = []
	children = derive_children(word,d)
	print('word:', word, 'with children:', children)
	for child in children:
		if reduce(child, d):
			reducible_children.append(child)
			print('reducible_children:', reducible_children)
			reducible_words[word] = reducible_children
			return reducible_children

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
	#reduce(word, d)
	print('------------------------')
	print('result', reduce(word, d))

max_length = 0
for word in reducible_words:
	if reducible_words[word] != []:
		max_length = max(max_length, len(word))

for word in reducible_words:
	if len(word) == max_length:
		if reducible_words[word] != []:
			print_trail(word, reducible_words)


