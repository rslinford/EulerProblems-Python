import numpy as np

"""
Euler Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

answer = 0
the_answer = 142913828922
sum_of_primes = 0
prime = 2


def is_prime(n):
    for j in range(2, n):
        if (n % j) == 0:
            return False
    return True


def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n


while prime < 2000000:
    print("Prime %d" % prime)
    sum_of_primes += prime
    prime = next_prime(prime)

answer = sum_of_primes

print("Answer: %d" % answer)
if answer == the_answer:
    print("Pass")
else:
    print("Fail")
