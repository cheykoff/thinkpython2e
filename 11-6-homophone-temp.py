'''

- find 4 letter words with the same last 3 letters
- find 5 letter words with the 2 first letters equal to the first letters of the 4 letter words
- find homophone
- 

Create dictionary
open file
store all 4 letter words in a dictionary
with same 3 last letters
key: word
value: pronounciation

find homophones
invert dictionary
key: pronounciation
value: list with words

select homophones with at least two words with the same last 3 letters

for all these homophones
go through 5 letter word dictionary

output:
'w r aah k', 'wrack', 'rack', 'wack'

Filter for all 5 letter words
Create a dictionary with words as keys (strings) and pronounciations (strings) as values
Reverse lookup of each pronounciation and find other homophones

filre for all 4 letter words
find homophones with last 3 letters identical


Alternative: Inverse the dictionary, print the pronounciations with at least 3 values
'''

'''
TO DO: 
Check which 4 letter words have the last 3 in common
search for 5 letter words having the same pronounciation and the first 2 letters are identical to the 1st letter of 2 words
'''

def create_word_dictionary4():
	d = {}
	fin = open('pronounciation-dictionary-clean.txt')
	for line in fin:
		key_value = []
		key_value = line.split("  ")
		if len(key_value[0]) == 4:
			d[key_value[0]] = key_value[1].strip()
	return d

def create_word_dictionary45():
	d = {}
	fin = open('pronounciation-dictionary-clean.txt')
	for line in fin:
		key_value = []
		key_value = line.split("  ")
		if 3 < len(key_value[0]) < 6:
			d[key_value[0]] = key_value[1].strip()
	return d

def create_word_dictionary5():
	d = {}
	fin = open('pronounciation-dictionary-clean.txt')
	for line in fin:
		key_value = []
		key_value = line.split("  ")
		if len(key_value[0]) == 5:
			d[key_value[0]] = key_value[1].strip()
	return d

def invert_dict(d):
	inverse = {}
	for key in d:
		val = d[key]
		inverse.setdefault(val, []).append(key)
	return inverse

def find_homophones(inverse):
	count = 0
	homophones = {}
	number = 2
	for item in inverse:
		if len(inverse[item]) > number:
			homophones[item] = inverse[item]
			#print(homophones[item])
			count += 1
	print('number of pronounciations with more than', number, 'homophones:', count)
	return homophones

def last_three_letters_equal(homophones):
	equal_last_three_letters = {}
	count = 0
	for key in homophones:
		equal_last_three_letters[key] = []
		for i in range(len(homophones[key])):
			for j in range(len(homophones[key])):
				#print('homophones', homophones)
				for k in range (len(homophones[key])):
					if i != j and i != k and j != k and homophones[key][i][-3:] == homophones[key][j][-3:] and homophones[key][i][-3:] == homophones[key][k][-3:]:
						'''print('homophones:', homophones)
						print('key:', key)
						print('homophones[key]:', homophones[key])
						print('homophones[key][i]:', homophones[key][i])
						print('homophones[key][j]:', homophones[key][j])
						print('equal_last_three_letters:', equal_last_three_letters)
						print('equal_last_three_letters[key]:', equal_last_three_letters)
						'''
						if homophones[key][i] not in equal_last_three_letters[key]: 
							equal_last_three_letters[key].append(homophones[key][i])
							count += 1
					'''
					if homophones['n equal_last_three_letters:
						equal_last_three_letters[key] = homophones[key][i] #, homophones[key][j]]
					'''
					#print('3 letters', equal_last_three_letters)
	print('number of homophones with last three letters equal: ', count)
	return equal_last_three_letters

test_dict = {'a': ['abcd', 'bbcd', 'cbcd'], 'b': ['abce', 'bbce'], 'c': ['abcf', 'bbcg']}


#print('test', last_three_letters_equal(test_dict))

# print(create_word_dictionary4())
#print(invert_dict(create_word_dictionary4()))
#print('result', last_three_letters_equal(find_homophones(invert_dict(create_word_dictionary4()))))

#d = last_three_letters_equal(find_homophones(invert_dict(create_word_dictionary4())))
#d2 = (invert_dict(create_word_dictionary5()))
d45 = last_three_letters_equal(find_homophones(invert_dict(create_word_dictionary45())))

count = 0
for item in d45:
	sum = 0
	if len(d45[item]) > 2:
		for i in range(len(d45[item])):
			sum += len(d45[item][i])
			#print(sum)
			if sum == (13 or 17 or 18):
				for j in range(len(d45[item])):
					if len(d45[item][j]) == 5:
						for k in range(len(d45[item])):
							if j != k and d45[item][j][0] == d45[item][k][0]:
								for m in range(len(d45[item])):
									if j != m and d45[item][j][1] == d45[item][m][0]:
										print('pronounciation:', item, '\nwords:', d45[item][j], d45[item][k], d45[item][m])
										count += 1

print('number of pronounciations with at least 3 homophones with all conditions true', count)

# print(d2)

