import numpy as np

"""
Euler Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit 
numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
answer = 0
the_answer = 906609

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        ps = str(product)
        if ps[0] == ps[-1] and ps[1] == ps[-2] and ps[2] == ps[-3]:
            if product > answer:
                print(str(i) + " x " + str(j) + " = " + str(product))
                answer = product

print("Answer: " + str(answer))
if answer == the_answer:
    print("Pass")
else:
    print("Fail")
