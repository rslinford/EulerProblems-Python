import time
from math import factorial

"""
Euler Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

answer = 0
the_answer = 137846528820
start_time = time.time()


def calc_number_paths(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


answer = calc_number_paths(40, 20)

elapsed_time = time.time() - start_time
print("Answer %d in %d seconds" % (answer, elapsed_time))
if answer == the_answer:
    print("Pass")
else:
    print("Fail")
