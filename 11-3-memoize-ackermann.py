# create an empty dictionary
known = {}

def ackermann(m, n):
	if m == 0:
		return n + 1	
	if n == 0:
		return ackermann(m-1, 1)
	if m and n in known:
		# use key tuple (m, n) to look up if there is a value stored
		return known[m, n]
	else:
		# store key tuple (m, n) with value
		known[m, n] = ackermann(m-1, ackermann(m, n-1))
		return known [m, n]

print(ackermann(3, 4))
print(type((1,2))