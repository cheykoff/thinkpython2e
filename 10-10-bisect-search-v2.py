'''
solution approach:
save words in list
reverse word and search in word list
'''

from bisect import bisect_left

def save_words_in_list():
	word_list = []
	fin = open('words-a-d.txt')
	for line in fin:
		word_list.append(line.strip())
	return word_list

def rev_word(word):
	return word[::-1]

def bi_sect_search(word, word_list):
	lo = 0
	hi = len(word_list)
	while hi - lo > 0:
		mid = (lo+hi)//2
		if word == word_list[mid]:
			return True
		elif word < word_list[mid]:
			hi = mid
		else:
			lo = mid + 1
	return False

bisect_left


def check_words(word_list):
	count = 0
	for word in word_list:
		if bi_sect_search(rev_word(word), save_words_in_list()):
			print(word, rev_word(word))
			count += 1
	print(count)


#check_words(save_words_in_list())