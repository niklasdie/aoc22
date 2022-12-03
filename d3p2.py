import aocd
import numpy as np
from aocd.models import Puzzle

ex_in = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

puzzle = Puzzle(day=3, year=2022)
or_in = puzzle.input_data
#or_in = ex_in
res = 0
lines = or_in.split("\n")
counter = np.zeros([53])
for i in range(len(lines)):
    line = lines[i]
    if i % 3 == 0:
        counter = np.zeros([53])
    for c in line:
        if i % 3 == 0:
            if c.isupper():
                counter[ord(c) - 38] = 1
            else:
                counter[ord(c) - 96] = 1
        if i % 3 == 1:
            if c.isupper():
                if counter[ord(c) - 38] == 1:
                    counter[ord(c) - 38] = 2
            else:
                if counter[ord(c) - 96] == 1:
                    counter[ord(c) - 96] = 2
        if i % 3 == 2:
            if c.isupper():
                if counter[ord(c) - 38] == 2:
                    counter[ord(c) - 38] = 3
            else:
                if counter[ord(c) - 96] == 2:
                    counter[ord(c) - 96] = 3
    if i % 3 == 2:
        for i in range(len(counter)):
            if counter[i] == 3:
                res += i
print(res)
puzzle.answer_b = res
