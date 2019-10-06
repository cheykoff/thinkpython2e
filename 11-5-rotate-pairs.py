'''
get a list of words
create an empty dictionary
???
questions:
store all possible rotations in the dictionary


ideas:
check the length
compare the first letter and use the difference to check the others

'''
def create_wordlist():
	wordlist = {}
	fin = open('words-long.txt')
	for line in fin:
		if len(line.strip()) < 4:
			wordlist[line.strip()] = None
	return wordlist 

def find_rotate_pairs(wordlist):
	d = {}
	for word in wordlist:
		rotated_words = rotate_word(word)
		for i in range (1, 26):
			d[rotated_words[i]] = 1
	for word in wordlist:
		if word in d:
			print(word)

def rotate_word(word):
	rotated_words = []
	for i in range(0, 26):
		new_word = ''
		for letter in word:
			new_ord = ord(letter) + i
			if new_ord > 122:
				new_ord -= 26
			new_letter = chr(new_ord)
			new_word += new_letter
		rotated_words.append(new_word)
	return rotated_words

find_rotate_pairs(create_wordlist())