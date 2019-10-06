'''
problem: 
input: text file with words
output: all words which can be transformed into another word by changing two letters (metathesis)

solution approach:
save words into dictionary with signature as key and anagrams as list {'acr': ['arc', 'car']}
for each list of anagrams (=values of the dictionary) compare each word with all other words within the list
if all but two letters are in the same place then it is a metathesis
print the metathesis_pairs
'''

def read_file():
	d_signature_anagrams = {}
	with open('words-long.txt') as fin:
		for line in fin:
			word = line.strip()
			if word.isalpha():
				word = word.lower()
				key = tuple(sorted(word))
				d_signature_anagrams[key] = d_signature_anagrams.get(key,[]) + [word]
	return d_signature_anagrams

def find_and_print_metathesis_pairs_from_dictionary(d_signature_anagrams):
	count_metathesis_pairs = 0
	list_of_anagrams = list(d_signature_anagrams.values())
	for anagrams in list_of_anagrams:
		metathesis_pairs = find_metathesis_pairs_within_anagrams(anagrams)
		if len(metathesis_pairs):
			for item in metathesis_pairs:
				print(item[0],item[1])
				count_metathesis_pairs += 1
	print(count_metathesis_pairs, 'pairs of metathesis were found') 

def word_distance(word1, word2):
	count = 0
	for c1, c2 in zip(word1, word2):
		if c1 != c2:
			count += 1
	return count

def find_metathesis_pairs_within_anagrams(anagrams):
	metathesis_pairs = []
	for word1 in anagrams:
		for word2 in anagrams:
			if word1 < word2 and word_distance(word1, word2) == 2:
				metathesis_pairs.append((word1, word2))
	return metathesis_pairs

d_signature_anagrams = read_file()
find_and_print_metathesis_pairs_from_dictionary(d_signature_anagrams)