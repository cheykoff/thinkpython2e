'''
store each item of the list as a key in the dictionary
for each new item check if it is already in the dictionary

'''
def has_duplicates(l):
	# create an empty dictionary
	d = {}
	# go through all items in the list
	for i in l:
		print('check if', i, 'is in', d)
		# is the item in the dictionary (hint: the first time it cannot be)
		if i in d:
			return True
		else:
			# store the item in the dictionary (the value does not matter)
			d[i] = 1
	return False

l = ['one', 'two', 'three', 'four', 'one']
print(has_duplicates(l))