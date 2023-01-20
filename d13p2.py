import collections.abc
import time
from aocd.models import Puzzle
from ast import literal_eval

ex_in = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

puzzle = Puzzle(day=13, year=2022)
or_in = puzzle.input_data
# or_in = ex_in

st = time.process_time()

or_in += "\n"
comp = []
res = 0


def compare(comp):
    if not isinstance(comp[0], collections.abc.Sequence):
        comp[0] = [comp[0]]
    elif not isinstance(comp[1], collections.abc.Sequence):
        comp[1] = [comp[1]]
    res = 0
    min_len = len(comp[0])
    if min_len > len(comp[1]):
        min_len = len(comp[1])
    for i in range(min_len):
        if isinstance(comp[0][i], collections.abc.Sequence) and isinstance(comp[1][i], collections.abc.Sequence):
            comp1 = [comp[0][i], comp[1][i]]
            res = compare(comp1)
        elif isinstance(comp[0][i], collections.abc.Sequence):
            comp1 = [comp[0][i], comp[1][i]]
            res = compare(comp1)
        elif isinstance(comp[1][i], collections.abc.Sequence):
            comp1 = [comp[0][i], comp[1][i]]
            res = compare(comp1)
        elif comp[0][i] < comp[1][i]:
            return 1
        elif comp[0][i] > comp[1][i]:
            return -2
        if res != 0:
            return res
    if len(comp[0]) == len(comp[1]):
        return 0
    if len(comp[0]) < len(comp[1]):
        return 1
    else:
        return -1


i_2 = 1
i_6 = 2
for c in or_in.split("\n"):
    if c != "":
        comp = literal_eval(c)
        if compare([comp, [[2]]]) == 1:
            i_2 += 1
            i_6 += 1
        else:
            if compare([comp, [[6]]]) == 1:
                i_6 += 1

print(f"res = {i_2 * i_6}")
print('Time:', time.process_time() - st, 'seconds')

puzzle.answer_b = i_2 * i_6
