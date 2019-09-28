'''
problem:
input: word as string
output: characters of the word sorted by alphabet in a list

solution approach:
create an empty list
take each letter and add it to the list
sort the list
'''
def order_by_letter(word):
	letters = []
	for char in word:
		letters.append(char)
		letters = sorted(letters)
	return letters

word = 'elementary'
letters = order_by_letter(word)
print(letters)