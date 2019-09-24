def read_word_list_into_list():
	word_list = []
	fin = open('anagrams-test.txt')
	for line in fin:
		word_list.append(line.strip())
	return word_list

def letter_to_number(char):
	char = char.lower()
	number = ord(char) - 97
	return number

def get_nth_prime(n):
	primes = []
	i = 2
	count = 0
	while count <= n:
		j = 2
		is_prime = True
		while j < i:
			if i % j == 0:
				is_prime = False	
			j += 1
		if is_prime:
			primes.append(i)
			count += 1
		i += 1
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