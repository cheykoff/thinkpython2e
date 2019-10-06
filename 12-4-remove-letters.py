'''
problem:
input: file with words (one per line)
output: longest word which can be always reduced (one letter at a time) to a valid word until it only has one letter left

solution approach:
find for each word all potential words which can be derived from it by reducing each of its letters
d = {'ghost': ['ghos', 'ghot', 'ghst', 'gost', 'host']}
after all words have this list
start with 'a' (and then with 'I') and find words which have one letter more
do this recursevily no more words are found
go through these words and get the longest 
'''
with open('words.txt') as file:
	for line in file:
		word = line.strip()
		if len(word) == 1:
			print(word)