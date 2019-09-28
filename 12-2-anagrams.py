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

def read_file_into_list_of_words():
	word_list = []
	fin = open('words-long.txt')
	for line in fin:
		word_list.append(line.strip())
	return word_list

def sort_letters(word):
	letters = []
	for char in word:
		letters.append(char)
	letters = sorted(letters)
	return letters

def sort_letters_for_all_words(word_list):
	word_and_sorted_letters_list = []
	for word in word_list:
		sorted_letters = sort_letters(word)
		word_and_sorted_letters_list.append((sorted_letters, word))
	return word_and_sorted_letters_list

def sort_list_of_words_and_letters(word_and_sorted_letters_list):
	sorted_list = sorted(word_and_sorted_letters_list)
	return sorted_list

def find_anagrams(l):
	i = 0
	anagrams = []
	for i in range(len(l)):
		#print(l[i][1], end=': ')
		j = 1
		list_of_anagrams = []
		if i + j < len(l):
			while l[i][0] == l[i+j][0]:
				#print(l[i+j][1], end=', ')
				list_of_anagrams.append(l[i+j][1])
				j += 1
			j = -1
			while l[i][0] == l[i+j][0]:
				#print(l[i+j][1], end=', ')
				list_of_anagrams.append(l[i+j][1])
				j -= 1
		#print('')
		anagrams.append((l[i][1], list_of_anagrams))
	return anagrams

def print_word_and_anagrams(anagrams):
	print('word: anagrams')
	anagrams = sorted(anagrams)
	for word_and_anagrams in anagrams:
		print(word_and_anagrams[0], end=': ')
		if word_and_anagrams[1] == []:
			print('---', end='')
		else:
			for anagram in word_and_anagrams[1]:
				print(anagram, end=', ')
		print('')

word_list = read_file_into_list_of_words()
word_and_sorted_letters_list = sort_letters_for_all_words(word_list)
sorted_list = sort_list_of_words_and_letters(word_and_sorted_letters_list)
anagrams = find_anagrams(sorted_list)
print_word_and_anagrams(anagrams)
