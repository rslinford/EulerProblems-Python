import numpy as np

"""
Euler Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
3**2 + 4**2 = 5**2  for example (3, 4, 5) is the triplet.
 
Sum of triplet 3 * 4 * 5 = 60 // we are looking the product abc. Example = 60. But abc where a + b + c = 1000.
if Sum of triplet = 1000 the product abc is == ? 

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

1) Find pythagorean triplets starting with 3,4,5
2) Test for the one where a+b+c=1000
3) Calculate a*b*c => answer
"""

answer = 0
the_answer = 31875000
the_sum = 1000

a = 3
b = 4
c = 5

while answer == 0:
    # Is a,b, and c pythagorean triplet?
    if a ** 2 + b ** 2 == c ** 2:
        print("Triplet (%d, %d, %d)" % (a, b, c))
        # Is the triplet the right one?
        a_sum = a + b + c
        print("%d + %d + %d = %d" % (a, b, c, a_sum))
        if a_sum == the_sum:
            answer = a * b * c
            break

    # Roll forward to next candidate triplet wrapping at the_sum as upper boundary.
    c += 1
    if c > the_sum:
        b += 1
        c = b + 1
        if b > the_sum:
            a += 1
            b = a + 1
            c = b + 1

print("Answer: %d" % answer)
if answer == the_answer:
    print("Pass")
else:
    print("Fail")
