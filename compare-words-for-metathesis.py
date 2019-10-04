words = ['yest', 'stey', 'stye', 'tyes']

for i, word in enumerate(words):
	for j, word in enumerate(words):
		count = 0
		for k, letter in enumerate(words[i]):
			if words[i][k] != words[j][k]:
				count += 1
		if count == 2:
			print(words[i], 'and', words[j], 'are metatheses')


