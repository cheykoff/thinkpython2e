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
			count_metathesis_pairs += len(metathesis_pairs)
			print(metathesis_pairs)
	print(int(count_metathesis_pairs/2), 'pairs of metathesis were found') 

def find_metathesis_pairs_within_anagrams(anagrams):
	metathesis_pairs = []
	for i, word in enumerate(anagrams):
		for j, word in enumerate(anagrams):
			diff_letter_count = 0
			for k, letter in enumerate(anagrams[i]):
				if anagrams[i][k] != anagrams[j][k]:
					diff_letter_count += 1
			if diff_letter_count == 2:
				metathesis_pairs.append((anagrams[i],anagrams[j]))
	return metathesis_pairs

d_signature_anagrams = read_file()
find_and_print_metathesis_pairs_from_dictionary(d_signature_anagrams)