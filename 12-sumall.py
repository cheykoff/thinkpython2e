def sum_all(*args):
	sum = 0
	for i in args:
		sum += i
	return sum

print(sum_all(1,2,3,3))
