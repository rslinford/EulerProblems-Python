import time
from math import factorial

"""
Euler Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value 
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

answer = 0
the_answer = 871198282
start_time = time.time()


def alpha_value(name):
    letters = list(name)
    letters = [ord(x) - 64 for x in letters]
    return sum(letters)


def name_score(place, name):
    return place * alpha_value(name)


with open('p022_names.txt') as f:
    a = f.read()
a = a.strip().split(',')
a = [x[1:-1] for x in a]
a.sort()

score_sum = 0
ordinal = 0
for x in a:
    ordinal += 1
    score_sum += name_score(ordinal, x)

answer = score_sum
elapsed_time = time.time() - start_time
print("Answer %d in %d seconds" % (answer, elapsed_time))
if answer == the_answer:
    print("Pass")
else:
    print("Fail")
