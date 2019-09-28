'''
Problem:
Input: word list (one word per line)
Output: list of anagrams (word and all its anagrams per line)

Solution approach:
create a list of words from txt file
for each word sort the letters by the alphabet 
store the word and the sorted letters in a tuple in a list
sort the list by the sorted letters
compare the sorted letters of each tuple with the tuples before and after
all sorted letters which are equal are anagrams
print each word and anagrams in one line
'''

def read_list():
	words = []
	fin = open('words-long.txt')
	for line in fin:
		word = line.strip()
		if word.isalpha():
			word = word.lower()
			words.append(word)
	return words	

def sort_letters(word):
	letters = []
	for char in word:
		letters.append(char)
	letters = sorted(letters)
	return letters

def create_tuple_list(words):
	tuple_list = []
	for word in words:
		sorted_letters = sort_letters(word)
		tuple_list.append((sorted_letters, word))
	return tuple_list

def sort_list(tuple_list):
	sorted_list = sorted(tuple_list)
	return sorted_list

def find_anagrams(sorted_list):
	i = 0
	all_anagrams = []
	for i in range(len(sorted_list)):
		j = 1
		anagrams = []
		if i + j < len(sorted_list):
			while sorted_list[i][0] == sorted_list[i+j][0]:
				anagrams.append(sorted_list[i+j][1])
				j += 1
			j = -1
			while sorted_list[i][0] == sorted_list[i+j][0]:
				anagrams.append(sorted_list[i+j][1])
				j -= 1
		if anagrams != []:
			all_anagrams.append((sorted_list[i][1], anagrams))
	return all_anagrams

def print_anagrams(anagrams):
	count = 0
	max_anagrams = 0
	min_anagrams_to_print = 10
	list_min_anagrams = []
	anagrams = sorted(anagrams)
	for line in anagrams:
		count += 1
		max_anagrams = max(max_anagrams, len(line[1]) + 1)
		if len(line[1]) + 1 >= min_anagrams_to_print:
			list_min_anagrams.append((line[0], line[1]))
	print('Total number of anagrams:', count)
	print('The maximum number of words with the same letters is', max_anagrams)
	print('Words with at least', min_anagrams_to_print, 'anagrams:', len(list_min_anagrams))
	for line in list_min_anagrams:
		print(line[0], end=': ')
		for anagram in line[1]:
			print(anagram, end=', ')
		print('')

words = read_list()
tuple_list = create_tuple_list(words)
sorted_list = sort_list(tuple_list)
anagrams = find_anagrams(sorted_list)
print_anagrams(anagrams)