import time
from math import factorial

"""
Euler Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the  
sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum 
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two 
abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as 
the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is 
known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

answer = 0
the_answer = 4179871
start_time = time.time()
upper_limit = 28123  # from the problem description


def proper_divisors(n):
    divisors = list()
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors


def is_abundant(n):
    return n < sum(proper_divisors(n))


abundant_numbers = list()
for x in range(1, upper_limit):
    if is_abundant(x):
        abundant_numbers.append(x)

not_sum_of_two_abundants = [x for x in range(upper_limit)]

for x in abundant_numbers:
    for y in abundant_numbers:
        s = x + y
        if s < upper_limit:
            # print("not the sum of two abundants " + str(s))
            not_sum_of_two_abundants[s] = 0

answer = sum(not_sum_of_two_abundants)

elapsed_time = time.time() - start_time
print("Answer %d in %d seconds" % (answer, elapsed_time))
if answer == the_answer:
    print("Pass")
else:
    print("Fail")
