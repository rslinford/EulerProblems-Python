import time
import re
from decimal import *

"""
Euler Problem 27

Euler discovered the remarkable quadratic formula:

   n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values . However, when  is divisible 
by 41, and certainly when  is clearly divisible by 41.

The incredible formula

   n**2 -79*n + 1601
  
was discovered, which produces 80 primes for the consecutive values . The product of the 
coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

   n**2 + a*n + b, where |a| < 1000 and |b| <= 1000

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes 
for consecutive values of n, starting with n=0.

"""

answer = 0
the_answer = -59231
start_time = time.time()


def is_prime(x):
    for j in range(2, x):
        if (x % j) == 0:
            return False
    return True


a_coef = 0
b_coef = 0
n_val = 0
a_coef_max = 0
b_coef_max = 0
n_val_max = 0
max_consecutive_primes = 0
index = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        consecutive_primes = True
        n = -1
        while consecutive_primes:
            index += 1
            n += 1
            prime_candidate = n ** 2 + a * n + b
            consecutive_primes = is_prime(prime_candidate)
            if not consecutive_primes:
                if (n_val + 1) > max_consecutive_primes:
                    max_consecutive_primes = n_val + 1
                    a_coef_max = a_coef
                    b_coef_max = b_coef
                    n_val_max = n_val
                    print("a(%d) b(%d) n(%d)" % (a_coef, b_coef, n_val))
            else:
                a_coef = a
                b_coef = b
                n_val = n
                # if index % 10000000 == 0:
                #     print("a(%d) b(%d) n(%d) => %d prime(%s) max_consecutive_prime(%d)" %
                #           (a, b, n, prime_candidate, str(consecutive_primes), max_consecutive_primes))

print("a(%d) b(%d) n(%d) gives a max consecutive prime of %d" % (a_coef_max, b_coef_max, n_val_max,
                                                                 max_consecutive_primes))
answer = a_coef_max * b_coef_max

elapsed_time = time.time() - start_time
print("Answer %s in %d seconds" % (answer, elapsed_time))
if answer == the_answer:
    print("Pass")
else:
    print("Fail")
