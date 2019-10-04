'''
Problem:
Input: word list (one word per line)
Output: the collection of 8 letters that form the most words (which are anagrams)

Solution approach:
create a list of words of 8 letters from txt file
create a dictionary
for each word 
	add it to the dictionary with the letters as a tuple in alphapetical order as key and the word as list item for the value
create a second dictionary which adds the number of the anagrams to the key. 
sort the second dictionary
print the values 
'''
def read_list():
	'''input: 
	text file
	output: dictionary {'acr': ['arc', 'car']} 
	'''
	d = {} 
	fin = open('words-long.txt')
	for line in fin:
		word = line.strip()
		if word.isalpha() and len(word) == 8:
			word = word.lower()
			key = tuple(sorted(word))
			d[key] = d.get(key,[]) + [word]
	return d

def add_len(d):
	'''input: dictionary {'acr': ['arc', 'car']} 
	output: dictionary {(2, 'acr'): ['arc', 'car']}
	'''
	d2 = {}
	for key in d:
		key2 = (len(d[key]), key)
		d2[key2] = d[key]
	return d2

def print_longest_anagrams(d):
	
	count = 0
	max_len = 0	
	print('The longest anagrams with 8 letters are:')
	length = max_len
	for key in sorted(d, reverse=True):
		anagram = d[key]
		if len(anagram) >= max_len:
			print(len(anagram), anagram)
			count += 1
			max_len = max(max_len, len(anagram))

dictionary = read_list()
dictionary2 = add_len(dictionary)
print_longest_anagrams(dictionary2)