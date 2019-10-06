def create_word_list():
	fin = open('words.txt')
	word_list = []
	for line in fin:
		word_list.append(line.strip())
	return word_list

def reverse_word(word):
	return word[::-1]

def bisect_right(search_list, word, lo=0, hi=None):
	if lo < 0:
		raise ValueError('lo must be non-negative')
	if hi is None:
		hi = len(search_list)
	reps = 0
	while lo < hi:
		reps += 1
		mid = (lo + hi) // 2
		if word < search_list[mid]:
			hi = mid
		else:
			lo = mid + 1
	if word == search_list[lo-1]:
		return True
	else:
		return False
	return lo

def find_reversed_words(word_list):
	count = 0
	for word in word_list:
		if bisect_right(word_list, reverse_word(word)):
			print(word, reverse_word(word))
			count += 1
	print(count)

find_reversed_words(create_word_list())