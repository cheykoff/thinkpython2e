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
		word = line.strip()
		if word.isalpha():
			word = word.lower()
			word_list.append(word)
	return word_list	

def sort_letters(word):
	letters = []
	for char in word:
		letters.append(char)
	letters = sorted(letters)
	return letters

def sort_letters_for_all_words(word_list):
	sorted_letters_and_words_list = []
	for word in word_list:
		sorted_letters = sort_letters(word)
		sorted_letters_and_words_list.append((sorted_letters, word))
	return sorted_letters_and_words_list
ö
def sort_list_of_sorted_letters_and_words(sorted_letters_and_words_list):
	sorted_list_of_sorted_letters_and_words = sorted(sorted_letters_and_words_list)
	return sorted_list_of_sorted_letters_and_words

def find_anagrams(sorted_list_of_sorted_letters_and_words):
	int_word = 0
	anagrams = []
	for int_word in range(len(sorted_list_of_sorted_letters_and_words)):
		int_diff = 1
		list_of_anagrams = []
		if int_word + int_diff < len(sorted_list_of_sorted_letters_and_words):
			while sorted_list_of_sorted_letters_and_words[int_word][0] == sorted_list_of_sorted_letters_and_words[int_word+int_diff][0]:
				list_of_anagrams.append(sorted_list_of_sorted_letters_and_words[int_word+int_diff][1])
				int_diff += 1
			int_diff = -1
			while sorted_list_of_sorted_letters_and_words[int_word][0] == sorted_list_of_sorted_letters_and_words[int_word+int_diff][0]:
				list_of_anagrams.append(sorted_list_of_sorted_letters_and_words[int_word+int_diff][1])
				int_diff -= 1
		if list_of_anagrams != []:
			anagrams.append((sorted_list_of_sorted_letters_and_words[int_word][1], list_of_anagrams))
	return anagrams

def print_word_and_anagrams(anagrams):
	count_anagrams = 0
	max_anagrams = 0
	min_anagrams_to_print = 10
	list_min_anagrams = []
	anagrams = sorted(anagrams)
	for word_and_anagrams in anagrams:
		count_anagrams += 1
		max_anagrams = max(max_anagrams, len(word_and_anagrams[1]) + 1)
		if len(word_and_anagrams[1]) + 1 >= min_anagrams_to_print:
			list_min_anagrams.append((word_and_anagrams[0], word_and_anagrams[1]))
	print('Total number of anagrams:', count_anagrams)
	print('The maximum number of words with the same letters is', max_anagrams)
	print('Words with at least', min_anagrams_to_print, 'anagrams:', len(list_min_anagrams))
	for word_with_min_anagrams in list_min_anagrams:
		print(word_with_min_anagrams[0], end=': ')
		for anagram in word_with_min_anagrams[1]:
			print(anagram, end=', ')
		print('')

word_list = read_file_into_list_of_words()
sorted_letters_and_words_list = sort_letters_for_all_words(word_list)
sorted_list_of_sorted_letters_and_words = sort_list_of_sorted_letters_and_words(sorted_letters_and_words_list)
anagrams = find_anagrams(sorted_list_of_sorted_letters_and_words)
print_word_and_anagrams(anagrams)