'''
Problem:
Input: word list (one word per line)
Output: anagrams most words to least words

Solution approach:
create a list of words from txt file
create a dictionary
for each word 
	add it to the dictionary with the letters as a tuple in alphapetical order as key and the word as list item for the value
create a second dictionary which adds the number of the anagrams to the key. 
sort the second dictionary
print the values 
'''
def read_list():
	d = {} 
	fin = open('words-long.txt')
	for line in fin:
		word = line.strip()
		if word.isalpha():
			word = word.lower()
			key = tuple(sorted(word))
			d[key] = d.get(key,[]) + [word]
	return d

def add_len(d):
	d2 = {}
	for key in d:
		key2 = (len(d[key]), key)
		d2[key2] = d[key]

	return d2

def print_anagrams(d):
	count = 0
	max_len = 0	
	print('Anagrams:')
	length = max_len
	for key in sorted(d, reverse=True):
		anagram = d[key]
		if len(anagram) > 1:
			print(d[key], len(anagram))
			count += 1
			max_len = max(max_len, len(anagram))
	print('There are', count, 'anagrams')
	print('The longest is', max_len)

dictionary = read_list()
dictionary2 = add_len(dictionary)
print_anagrams(dictionary2)