import numpy as np

"""
Euler Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
answer = 0
the_answer = 232792560

max_candidate = 1
for i in range(1, 21):
    max_candidate *= i
print("max_candidate %d" % max_candidate)

candidate = 2520
while candidate < max_candidate:
    is_divisible = True
    for i in range(2, 21):
        if candidate % i != 0:
            is_divisible = False
            break
    if is_divisible:
        print("divisible check PASSES on %d" % candidate)
        answer = candidate
        break
    else:
        if candidate % 10000000 == 0:
            print("divisible check fails on %d" % candidate)
    candidate += 1

print("Answer: %d" % answer)
if answer == the_answer:
    print("Pass")
else:
    print("Fail")
