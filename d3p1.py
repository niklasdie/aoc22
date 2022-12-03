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
# or_in = ex_in
res = 0
for line in or_in.split("\n"):
    a = line[:int(len(line) / 2)]
    b = line[int(len(line) / 2):]
    counter = np.zeros([53])
    for c in a:
        if c.isupper():
            counter[ord(c) - 38] = 1
        else:
            counter[ord(c) - 96] = 1
    for c in b:
        if c.isupper():
            if counter[ord(c) - 38] == 1:
                counter[ord(c) - 38] = 2
        else:
            if ord(c) != 32:
                if counter[ord(c) - 96] == 1:
                    counter[ord(c) - 96] = 2
    for i in range(len(counter)):
        if counter[i] == 2:
            res += i
print(res)
puzzle.answer_a = res
