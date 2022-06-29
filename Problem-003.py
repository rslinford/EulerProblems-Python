import numpy as np
"""
Euler Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
answer = 0
the_answer = 6857
number = 600851475143

for prime_factor in range(2, int(number ** 0.5) + 1):
    while number % prime_factor == 0:
        number /= prime_factor
        if number == 1 or number == prime_factor:
            answer = prime_factor
            break

print(answer)
if answer == the_answer:
    print("Pass")
else:
    print("Fail")
