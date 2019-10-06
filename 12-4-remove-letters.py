'''
problem:
input: file with words (one per line)
output: longest word which can be always reduced (one letter at a time) to a valid word until it only has one letter left
solution approach:

'''
with open('words.txt') as file:
	for line in file:
		word = line.strip()
		if len(word) == 1:
			print(word)