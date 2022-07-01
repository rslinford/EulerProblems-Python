import time

import numpy as np

"""
Euler Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been 
proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

answer = 0
the_answer = 837799
start_time = time.time()

"""
1) function: calculate chain for a given number
2) loop over range(1, 100000) as starting numbers
3) find longest chain
"""

"""
n → n/2 (n is even)
n → 3n + 1 (n is odd)
"""


def tally_chain_length(n):
    tally = 1
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n*3 + 1
        tally += 1

    return tally


number_of_longest_tally = 0
longest_tally = 0
for i in range(1, 1000000):
    x = tally_chain_length(i)
    if x > longest_tally:
        longest_tally = x
        number_of_longest_tally = i
        print("Longest so far Tally %d)  %d" % (i, longest_tally))

answer = number_of_longest_tally
elapsed_time = time.time() - start_time
print("Answer %d in %d seconds" % (answer, elapsed_time))
if answer == the_answer:
    print("Pass")
else:
    print("Fail")
