import time
from math import factorial

"""
Euler Problem 21

"""

answer = 0
the_answer = 648
start_time = time.time()



elapsed_time = time.time() - start_time
print("Answer %d in %d seconds" % (answer, elapsed_time))
if answer == the_answer:
    print("Pass")
else:
    print("Fail")
