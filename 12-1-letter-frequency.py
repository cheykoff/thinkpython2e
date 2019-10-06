'''
Problem:
Input: textfile
Output: letters sorted by frequency

Solution Approach
Load textfile
convert to string
Go through string and 
add each letter to the dictionary (letter is key and frequency is value)
if it is already in: increase the value
invert the dictionary so the frequency is the key and the letter is the value 
create a list and store the frequency and letter as tuples in the list
sort the list and reverse it
print the letter and frequency
'''

def text_to_string():
	s = ''
	fin = open('text-example3.txt')
	for line in fin:
		s = s + line
	return s

def create_dictionary(s):
	s = s.lower()
	d = {}
	for char in s:
		if char.isalpha():
			d[char] = d.get(char, 0) + 1
	return d

def invert_dictionary(d):
	d_inv = {}
	for key in d:
		val = d[key]
		if val not in d_inv:
			d_inv[val] = [key]
		else:
			d_inv[val].append(key)
	return d_inv

def sort_by_frequency(d):
	l = []
	for char in d:
		l.append((char, d[char]))
	l.sort()
	l.reverse()
	return l

def print_line_per_char(l):
	print('frequency of letters:')
	for item in l:
		print(item[1][0], ':', item[0])

print_line_per_char(sort_by_frequency(invert_dictionary(create_dictionary(text_to_string()))))
