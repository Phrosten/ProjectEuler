# Even Fibonacci numbers

## Task

Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, &#x2026;

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.

## Solution

``` python
fib = [1, 2]

result = 2
while fib[-1] + fib[-2] <= 4000000:
    fib.append(fib[-1] + fib[-2])
    if fib[-1] % 2 == 0:
        result += fib[-1]

print(result)

```

## Result

    4613732