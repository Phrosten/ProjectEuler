# Largest Prime Factor

## Task

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

## Solution

``` python
import math

primes = []

def prime_factor(n):
if is_prime(n):
    return int(n)

factors = []
for i in range(2, math.ceil(math.sqrt(n))):
    if n / i == math.floor(n / i):
	factors.append(i)
	f = prime_factor(n / i)
	if type(f) == list:
	    factors += f
	else:
	    factors.append(f)
	break
return factors

def is_prime(n):
if n in primes:
    return True

for i in range(2, math.ceil(math.sqrt(n))):
    if n % i == 0:
	return False
primes.append(n)
return True

print(prime_factor(600851475143)[-1])
```

## Result

    6857
