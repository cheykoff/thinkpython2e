'''
how to find a prime:
try to divide the number by all primes smaller or equal to the square root of the number
if it divides by one of them it is no prime
if not it is a prime

potential idea: 
create a dictionary with all number 0..n as keys and True/False as value - if it is a prime or not
'''
def get_nth_prime(n):
	primes = []
	number = 2
	count = 0
	while count <= n:
		is_prime = True
		for prime in primes:
			if prime <= number**0.5 and is_prime:
				if number % prime == 0:
					is_prime = False
		if is_prime:
			primes.append(number)
			count += 1
		number += 1
	return primes[n]

nth_prime = get_nth_prime(100)
print(nth_prime)