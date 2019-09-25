'''
how to find a prime:
try to divide the number by all primes smaller or equal to the square root of the number
if it divides by one of them it is no prime
if not it is a prime

idea: create a dictionary with all number 0..n as keys and True/False as value - if it is a prime or not
idea: use the list of primes to only divide the number by those primes 
'''
def get_nth_prime(n):
	numbers = {}
	primes = []
	i = 2
	count = 0
	is_prime = True
	while count <= n :
		j = 2
		is_prime = True
		#print('number:', i, 'divide by', j, 'residual:', i%j)
		while j < i**0.5 and is_prime:
			print('number:', i, 'divide by', j, 'residual:', i%j)
			if i % j == 0:
				is_prime = False
			j += 1
		if is_prime:
			print('number:', i, 'divide by', j, 'residual:', i%j)
			primes.append(i)
			count += 1
		i += 1
	return primes

primes = get_nth_prime(30)
print(primes)