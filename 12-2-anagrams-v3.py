'''
Problem:
Input: word list (one word per line)
Output: anagrams

Solution approach:
create a list of words from txt file
create a dictionary
for each word 
	add it to the dictionary with the letters as a tuple in alphapetical order as key and the word as list item for the value
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

def print_anagrams(d):
	count = 0
	for key in d:
		anagrams = d[key]
		if len(anagrams) > 1:
			print(d[key])
			count += 1
	print(count, 'anagrams')


dictionary = read_list()
print_anagrams(dictionary)