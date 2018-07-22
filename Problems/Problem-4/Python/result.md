# Largest palindrome product

## Task

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

## Solution

``` python

import math

def is_palindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    return False

palindromes = []

x = 999
while x >= 100:
    y = 999
    while y >= 100:
        if is_palindrome(x * y):
            palindromes.append(x * y)
        y -= 1
    x -= 1

palindromes.sort()
print(palindromes[-1])

```

## Result

    906609
