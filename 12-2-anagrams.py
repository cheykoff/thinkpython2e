'''
Problem:
Input: word list (one word per line)
Output: list of anagrams (word and all its anagrams per line)

Solution approach:
create a list of words from txt file
map each word to a product of primes 
	convert each letter of the alphabet into a distinct prime
	multiple the primes (letters) of a word 
compare the result with other words
print all words with the same product of primes
'''

def read_word_list_into_list():
	word_list = []
	fin = open('anagrams-test.txt')
	for line in fin:
		word_list.append(line.strip())
	return word_list

def letter_to_number(char):
	char = char.lower()
	number = ord(char) - 97 # a-z maps to 0-25
	return number

'''
how to find a prime:
try to divide the number by all primes smaller or equal to the square root of the number
if it divides by one of them it is no prime
if not it is a prime
'''

def get_nth_prime(n):
	primes = []
	number = 2
	count = 0
	while count <= n:
		is_prime = True
		for prime in primes:
			if prime <= number**0.5 and is_prime:
				if number % prime == 0:
					is_prime = False
		if is_prime:
			primes.append(number)
			count += 1
		number += 1
	return primes[n]

def get_prime_mult_for_string(s):
	prime_mult = 1
	for char in s:
		prime_mult = prime_mult * get_nth_prime(letter_to_number(char))
	return prime_mult

def map_word_list_to_prime_mult(word_list):
	l = []
	for word in word_list:
		t = (word, get_prime_mult_for_string(word))
		l.append(t)
	return l

def find_anagrams(l):
	for item in l:
		k = []
		for item2 in l:
			if item[1] == item2[1] and item != item2:
				k.append(item2[0])
		if len(k) > 0:
			print(item[0], 'has anagrams', k) 
		else:
			print(item[0], 'has no anagrams') 
	
word_list = read_word_list_into_list()	
prime_mult_list = map_word_list_to_prime_mult(word_list)
find_anagrams(prime_mult_list)