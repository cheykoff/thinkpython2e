'''
requirements
input: word list as a txt file
output: print all words from txt file that have anagrams with all their anagrams within the word list

solution
read a txt file and store the words in a list
search each word in the dictionary (bisect search)
	search for each word that is an anagram
print word and its anagrams

ideas:
dictionary with primes for each letter and value is a list of words
'''

def read_word_list_into_list():
	l = []
	fin = open('anagrams-test.txt')
	for line in fin:
		l.append(line.strip())
	print(l)

read_word_list_into_list()