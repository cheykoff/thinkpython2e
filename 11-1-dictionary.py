def dictionary():
	d = {}
	fin = open('words-long.txt')
	for line in fin:
		d[line.strip()] = d.get(line.strip(),0) + 1 
	return d


def lookup(dictionary, word):
	for key in dictionary:
		if key == word:
			return True
	return False

def lookup_words(words):
	word_in_dictionary = {}
	for word in words:
		if lookup(dictionary, word):
			word_in_dictionary[word] = True
		else:
			word_in_dictionary[word] = False
	return word_in_dictionary

def input_word():
	while input != 'exit':
		print('Type "exit" to end the program')
		word = input('Please enter a word: ')
		print(word)
		if lookup(dictionary, word):
			print(word, ' is in the dictionary')
		else:
			print(word, ' is not in the dictionary')

input_word()
dictionary = dictionary()
words = ('ABS', 'beta', 'carrot', 'sphinx')
print(lookup_words(words))
