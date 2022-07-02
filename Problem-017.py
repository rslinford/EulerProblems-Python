import time

"""
Euler Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British 
usage.
"""

answer = 0
the_answer = 21124
start_time = time.time()
"""
1) function for generating the words for a given number
2) function for counting letters
"""

numbers_dict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}


def generate_words(n):
    if n < 21:
        return numbers_dict[n]
    elif 20 < n < 100:
        tens = n // 10 * 10
        ones = n % 10
        ones_text = ""
        if ones > 0:
            ones_text = "-" + generate_words(ones)
        return numbers_dict[tens] + ones_text
    elif 100 <= n < 1000:
        hundreds = n // 100
        remainder = n - (hundreds*100)
        remainder_text = ""
        if remainder > 0:
            remainder_text = "and " + generate_words(remainder)
        return generate_words(hundreds) + " hundred " + remainder_text
    elif n >= 1000:
        return "one thousand"
    else:
        return "Number translation not found"


def count_letters(s: str):
    tally = 0
    for j in range(0, len(s)):
        if s[j] != ' ' and s[j] != '-':
            tally += 1
    return tally


letter_total = 0
for i in range(1, 1001):
    w = generate_words(i)
    print("%d - %s" % (i, w))
    c = count_letters(w)
    letter_total += c

answer = letter_total
elapsed_time = time.time() - start_time
print("Answer %d in %d seconds" % (answer, elapsed_time))
if answer == the_answer:
    print("Pass")
else:
    print("Fail")
