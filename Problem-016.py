import time

"""
Euler Problem 16
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""

answer = 0
the_answer = 1366
start_time = time.time()

number_str = str(2**1000)
sum_of_digits = 0

for i in range(0, len(number_str)):
    sum_of_digits += int(number_str[i])

answer = sum_of_digits
elapsed_time = time.time() - start_time
print("Answer %d in %d seconds" % (answer, elapsed_time))
if answer == the_answer:
    print("Pass")
else:
    print("Fail")
