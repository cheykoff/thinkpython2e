'''
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

def has_three_interlocks(word, word_list):
	if bi_sect_search(word[::3], word_list) and bi_sect_search(word[1::3], word_list) and bi_sect_search(word[2::3], word_list):
		print(word, word[::3], word[1::3], word[2::3])

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
	#max_len = 0
	for word in word_list:
		has_three_interlocks(word, word_list)
			#print(word, word[::3], word[1::3], word[2::3])
		count += 1
			#max_len = max(max_len, len(word))
	print(count)
	#print(max_len)


find_all_interlocks(create_word_list())

#sec_all_words(create_word_list())

#print(bi_sect_search('aa',create_word_list()))
# wip: compare sec words with list 