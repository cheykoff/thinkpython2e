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
	with open('words-long.txt') as fin:
		for line in fin:
			word = line.strip()
			if word.isalpha():
				word = word.lower()
				key = tuple(sorted(word))
				d[key] = d.get(key,[]) + [word]
	return d

def go_through_dictionary(d):
	count_metatheses = 0
	list_of_words = list(d.values())
	#print(list_of_words)
	for words in list_of_words:
		metatheses = find_metathesis(words)
		if len(metatheses):
			count_metatheses += len(metatheses)
			print(metatheses)
	print(int(count_metatheses/2), 'pairs of metatheses were found') 

def find_metathesis(words):
	metatheses = []
	for i, word in enumerate(words):
		for j, word in enumerate(words):
			diff_letter_count = 0
			for k, letter in enumerate(words[i]):
				if words[i][k] != words[j][k]:
					diff_letter_count += 1
			if diff_letter_count == 2:
				metatheses.append((words[i],words[j]))
	return metatheses
'''
def print_anagrams(d):
	for key in d:
		anagrams = d[key]
		if len(anagrams) > 1:
			print(d[key])
'''
dictionary = read_list()
go_through_dictionary(dictionary)