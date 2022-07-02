import itertools
import time
from math import factorial

"""
Euler Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 
1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The 
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

answer = ""
the_answer = "2783915460"
start_time = time.time()

permutation_list = list(itertools.permutations(range(0, 10)))
print("Millionth lexicographic permutation + " + str(permutation_list[999999]))

millionth = permutation_list[999999]
s = ""
for x in millionth:
    s += str(x)
answer = s

elapsed_time = time.time() - start_time
print("Answer %s in %d seconds" % (answer, elapsed_time))
if answer == the_answer:
    print("Pass")
else:
    print("Fail")
