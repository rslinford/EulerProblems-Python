import numpy as np

"""
Euler Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

answer = 0
the_answer = 104743


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


prime = 1
for i in range(1, 10002):
    prime = next_prime(prime)
    print("%d) Prime %d" % (i, prime))
answer = prime

print("Answer: %d" % answer)
if answer == the_answer:
    print("Pass")
else:
    print("Fail")
