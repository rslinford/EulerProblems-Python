import numpy as np

"""
Euler Problem 6
The sum of the squares of the first ten natural numbers is 385

The square of the sum of the first ten natural numbers is 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square
of the sum is 3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the 
square of the sum.
"""
answer = 0
the_answer = 25164150
sum_of_squares = 0
sum = 0
for i in range(1, 101):
    sum += i
    sum_of_squares += i**2
    print("i: %d sum: %d sum_of_squares: %d" % (i, sum, sum_of_squares))

sqr_of_sum = sum**2
answer = sqr_of_sum - sum_of_squares

print("Answer: %d" % answer)
if answer == the_answer:
    print("Pass")
else:
    print("Fail")
