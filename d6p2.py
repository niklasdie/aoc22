from aocd.models import Puzzle

ex_in = """bvwbjplbgvbhsrlpgdmjqwftvncz"""

puzzle = Puzzle(day=6, year=2022)
or_in = puzzle.input_data
# or_in = ex_in

def f():
    for i in range(len(or_in) - 13):
        sub_in = or_in[i:i + 14]
        for m in range(14):
            if sub_in.count(sub_in[m]) != 1:
                break
            else:
                if m == 13:
                    return i + 14


res = f()
print(res)
puzzle.answer_b = res
