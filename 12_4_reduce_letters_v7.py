def create_dictionary():
	d = {}
	with open ('words.txt') as file:
		for line in file:
			word = line.strip().lower()
			d[word] = []
	return d

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



def print_trail(word, d):
	if word == '':
		print('!!!')
	else:
		print(word, end=' ')
		child = d[word]
		print_trail(child[0], d)

d = create_dictionary()
#print('dictionary d - all words')
#print(d)

d2 = get_children(d)
#print('dictionary d2 all words with all children')
#print(d2)

d3 = filter_for_parents(d2)
#print('dictionary d3 all words which can be reduced at least once')
#print(d3)

reducible_words = {}
reducible_words[''] = ['']

def get_reducable_words(d):
	for word in d:
		reduce(word, d)

def reduce(word, d):
	if word in reducible_words:
		return reducible_words[word]
	res = []
	children = derive_children(word,d)
	for child in children:
		if reduce(child, d):
			res.append(child)
	reducible_words[word] = res
	return res

for word in d3:
	reduce(word, d3)

#print('reducible_words')
#print(reducible_words)

max_length = 0
for word in reducible_words:
	if reducible_words[word] != []:
		max_length = max(max_length, len(word))

for word in reducible_words:
	if len(word) == max_length:
		if reducible_words[word] != []:
			print_trail(word, reducible_words)


