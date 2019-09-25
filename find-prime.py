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
		#print('current primes:', primes)
		for prime in primes:
			if prime <= number**0.5 and is_prime:
				#print('check prime', prime, 'for', number)
				if number % prime == 0:
					#print('number', number, 'can be divided by', prime, 'so it is not a prime')
					is_prime = False
				else:
					#print('number', number, 'can not be divided by', prime, 'so it could be still a prime')
					pass
		if is_prime:
			#print(number, 'is a prime')
			primes.append(number)
			count += 1
		else:
			#print(number, 'is no prime')
			pass
		number += 1
	return primes[n]

primes = get_nth_prime(1)
print(primes)