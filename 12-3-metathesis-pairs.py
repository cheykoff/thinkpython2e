'''
problem: 
input: text file with words
output: all words which can be transformed into another word by changing two letters (metathesis)

solution approach:
save words into dictionary with signature as key and anagrams as list {'acr': ['arc', 'car']}
for each list of anagrams (=values of the dictionary) compare each word with the other words
if all but two letters are in the same place then it is a metathesis
print the metatheses
'''

def read_list():
	d = {}
	with open('anagrams-test.txt') as fin:
		for line in fin:
			word = line.strip()
			if word.isalpha():
				word = word.lower()
				key = tuple(sorted(word))
				d[key] = d.get(key,[]) + [word]
	return d

def get_word_through_dictionary(d):
	list_of_words = list(d.values())
	print(list_of_words)
	'''
	for words in list_of_words:
		find_metathesis(words)


def find_metathesis(words):
	for i, word in enumerate(words):
		for j, word in enumerate(words):
			count = 0
			for k, letter in enumerate(words[i]):
				if words[i][k] != words[j][k]:
					count += 1
			if count == 2:
				print(words[i], 'and', words[j], 'are metatheses')
'''
def print_anagrams(d):
	for key in d:
		anagrams = d[key]
		if len(anagrams) > 1:
			print(d[key])

dictionary = read_list()
get_word_through_dictionary(dictionary)
# find_metathesis(dictionary)
#print_anagrams(dictionary)
