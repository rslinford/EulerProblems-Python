import itertools
import time
from math import factorial

"""
Euler Problem 25
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

answer = 0
the_answer = 4782
start_time = time.time()

fibs = list()
fibs.append(1)
fibs.append(1)
number_of_digits = 0
index = 2
while number_of_digits != 1000:
    index += 1
    fibs.append(fibs[-1] + fibs[-2])
    s = str(fibs[-1])
    number_of_digits = len(s)
    if number_of_digits == 1000:
        answer = index
        print("%d) %s" % (index, s))

elapsed_time = time.time() - start_time
print("Answer %s in %d seconds" % (answer, elapsed_time))
if answer == the_answer:
    print("Pass")
else:
    print("Fail")
