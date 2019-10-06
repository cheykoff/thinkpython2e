'''
create dictionary d1 from file with spelling as key and pronounciation as value
invert dictionary d1 to d2 with pronounciation as key and list of possible spellings as value
create dictionary d3 with pronounciations as key and list of list as value. 
	first list 5 letter words (at least one list item), second list 4 letter words (at least two list items)
compare last 3 letters of 5 letter words with last 3 letters of 4 letter words
compare first two letters of 5 letter words with first letters of 4 letter words
'''

def create_dictionary():
	d1 = {}
	l1 = []
	fin = open('pronounciation-dictionary-short.txt')
	for line in fin:
		l1 = line.strip()
		l1 = l1.split('  ')
		#print(l1)
		d1[l1[0]] = l1[1]
	#print(d1)
	return d1

def invert_dictionary(d1):
	d2 ={}
	for key in d1:
		val = d1[key]
		d2.setdefault(val, []).append(key)
	#print(d2)
	return d2

def filter_dictionary_45_letters(d2):
	d3 = {}
	for key in d2:
		#print(key)
		for val in d2[key]:
			if len(val) == 5:
				d3.setdefault(key, []).append(val)
			elif len(val) == 4:
				d3.setdefault(key, []).append(val)

	print(d3)
d1_test = {'aa': 'a', 'ah': 'a', 'ee': 'e', 'eh': 'e'}
d2_test = invert_dictionary(d1_test)
d3_test = {'a': ['aaa', 'aaaa', 'aaah', 'aaaaa', 'aaaah'], 'e': ['eee', 'eeee', 'eeeh', 'eeeee']}

create_dictionary()
invert_dictionary(d1_test)
#print(invert_dictionary(create_dictionary()))
filter_dictionary_45_letters(d3_test)
