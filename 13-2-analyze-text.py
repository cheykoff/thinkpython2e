import string

def read_file():
	with open('faust.txt', encoding="utf-8") as file:
		word_count = 0
		d = {}
		for line in file:
			words = line.split()
			for word in words:
				word = word.strip(string.punctuation).strip(string.whitespace).lower()
				word = word.translate(trantab)
				if word.isalpha():
					d[word] = d.get(word, 0) + 1
					word_count += 1
	return d

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


c_in = '‚‘’„“”'
c_out = '\'\'\'\"\"\"'
trantab = str.maketrans(c_in, c_out)

d = read_file()
inv_d = invert_dict(d)
l = sorted(inv_d)
l.reverse()
for key in l:
	print(key, inv_d[key])