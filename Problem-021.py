import time
from math import factorial

"""
Euler Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable 
numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The 
proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

answer = 0
the_answer = 31626
start_time = time.time()


def proper_divisors(n):
    divisors = list()
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors


def is_amicable(n):
    candidate_amicable = sum(proper_divisors(n))
    if candidate_amicable == n:
        return False
    return sum(proper_divisors(candidate_amicable)) == n


amicable_sum = 0
for x in range(1, 10000):
    if is_amicable(x):
        print(str(x) + " is amicable with " + str(sum(proper_divisors(x))))
        amicable_sum += x

answer = amicable_sum

elapsed_time = time.time() - start_time
print("Answer %d in %d seconds" % (answer, elapsed_time))
if answer == the_answer:
    print("Pass")
else:
    print("Fail")
