def create_dictionary():
	d = {}
	with open ('words.txt') as file:
		for line in file:
			word = line.strip().lower()
			len_word = len(word)
			d[(len_word, word)] = []
	return d

def sort_dictionary_by_length(d):
	d2 = sorted(d)
	return d2

def add_reduced_words(d1, d2):
	for item in d2:
		word = item[1]
		for i in range(item[0]):
			word2 = word[0:i] + word[i+1:len(word)]
			if (len(word2), word2) in d1:
				d1[(len(word), word)].append(word2)
	return d1

def find_reducibles(d3):
	d4 = {}
	for key in d3:
		value = d3[key]
		for word2 in value:
			if (len(word2), word2) in d3:
				d4[key[1]] = True
			else:
				d4[key[1]] = False
	return d4

def print_all_reducible(d4):
	for key in d4:
		print(key)

def find_longest_reducible(d4):
	max_length = 0
	for key in d4:
		max_length = max(max_length, len(key))
	for key in d4:
		if len(key) == max_length:
			print(key)

d1 = create_dictionary()
#print(d1)

d2 = sort_dictionary_by_length(d1)
#print(d2)

d3 = add_reduced_words(d1, d2)
#print(d3)

d4 = find_reducibles(d3)
#print(d4)

#print_all_reducible(d4)

find_longest_reducible(d4)


