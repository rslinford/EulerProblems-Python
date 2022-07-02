import time
import re
from decimal import *

"""
Euler Problem 26
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 
are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring 
cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

answer = 0
the_answer = 983
start_time = time.time()


def displaymatch(match):
    if match is None:
        return 0

    return len(match.group(1))


length_of_cycle = 0
max_length = 0
d = 0
getcontext().prec = 2000

for i in range(1, 1000):
    fraction = 1 / Decimal(i)
    pattern = re.search(r"^\d\.\d*(\d{7,}?)(\1+)\d*?$", str(fraction))

    length_of_cycle = displaymatch(pattern)

    if length_of_cycle > max_length:
        max_length = length_of_cycle
        d = i

print(d)
answer = d

elapsed_time = time.time() - start_time
print("Answer %s in %d seconds" % (answer, elapsed_time))
if answer == the_answer:
    print("Pass")
else:
    print("Fail")
