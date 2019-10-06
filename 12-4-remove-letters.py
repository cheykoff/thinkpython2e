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

alternative:
find all words which have either an 'I'or an 'a' in it. The rest of words are not suitable.
sort all words by length
start with the longest word and try to reduce it by one letter at a time
if it works we have found the longest word (test words which are equally long)
if not go the next word
'''
def create_dictionary():
	with open('words.txt') as file:
		d = {}
		for line in file:
			word = line.strip()
			if len(word) == 2:
				print(word)
				d[word] = None
	return d

def reduce_word(word, d):
	for key in d:
		print(key)
		if word[1:3] == key:
			print(word)

word = 'zye'
dictionary = create_dictionary()

print(word)
print(dictionary)
reduce_word(word, dictionary)