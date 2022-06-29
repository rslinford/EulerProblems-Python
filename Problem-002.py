import numpy as np
"""
Euler Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.

"""
answer = 0
the_answer = 4613732

# Initialize dummy variable at zero for our sum
even_sum = 0
current_fibonacci = 2
previous_fibonacci = 1

while current_fibonacci <= 4000000:
    if current_fibonacci % 2 == 0:
        even_sum += current_fibonacci
    current_fibonacci += previous_fibonacci
    previous_fibonacci = current_fibonacci - previous_fibonacci

answer = even_sum
print(answer)
if answer == the_answer:
    print("Pass")
else:
    print("Fail")
