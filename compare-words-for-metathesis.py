words = ['yest', 'stey', 'stye', 'tyes']

i = 0
for i in range(len(words)):
	j = 0
	for j in range(len(words)):
		k = 0
		count = 0
		for k in range(len(words[i])):
			if words[i][k] != words[j][k]:
				count += 1
		if count == 2:
			print(words[i], 'and', words[j], 'are metatheses')


