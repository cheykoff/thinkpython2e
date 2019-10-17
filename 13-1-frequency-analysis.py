import string

def read_file():
	with open('bewerbung-katha-ms.txt', encoding="utf-8") as file:
		for line in file:
			words = line.split()
			for word in words:
				word = word.strip(string.punctuation).strip(string.whitespace).lower()
				word = word.translate(trantab)
				if word != '':
					print(word, end=' ')


c_in = '‚‘’„“”'
c_out = '\'\'\'\"\"\"'
trantab = str.maketrans(c_in, c_out)

read_file()