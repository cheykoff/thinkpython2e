'''
Option 1
for each word 
combine with all words
to create new word
compare each of the words with word list
O(n²log(n))

Option 2
for each word 
take every second letter
to create new word
compare to word list
if it is in
take the other letters
to create new word
compare to word list
O(n log(n))
'''

def create_word_list():
	fin = open('words.txt')
	word_list = []
	for line in fin:
		word_list.append(line.strip())
	return word_list

def get_every_second_letter(word, start):
	sec_word = ''
	i = 0
	while i < len(word):
		if (i + start) % 3 == 0:
			sec_word += word[i]
		i += 1
	return sec_word

def sec_all_words(word_list):
	for word in word_list:
		get_every_second_letter(word)

def bi_sect_search(word, word_list, lo=0, hi=None):
	hi = len(word_list)
	while lo < hi:
		mid = (lo + hi) // 2
		if word == word_list[mid]:
			return True
		if word < word_list[mid]:
			hi = mid
		else:
			lo = mid + 1
	return False

def find_all_interlocks(word_list):
	count = 0
	max_len = 0
	for word in word_list:
		if bi_sect_search(get_every_second_letter(word, 0), word_list):
			if bi_sect_search(get_every_second_letter(word, 1), word_list):
				if bi_sect_search(get_every_second_letter(word, 2), word_list):
					print(word, get_every_second_letter(word, 0), get_every_second_letter(word, 2), get_every_second_letter(word, 1))
					count += 1
					max_len = max(max_len, len(word))
	print(count)
	print(max_len)


find_all_interlocks(create_word_list())

#sec_all_words(create_word_list())

#print(bi_sect_search('aa',create_word_list()))
# wip: compare sec words with list 