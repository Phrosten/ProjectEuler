# Smallest multiple

## Task

2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

## Solution

``` python

found = False
num = 20

while not found:
    n = 20
    while n > 10:
        if not num % n == 0:
            break
        n -= 1
    if n == 10:
        found = True
        break
    num += 20

print(num)

```

## Result

    232792560
