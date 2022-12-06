from aocd.models import Puzzle

ex_in = """bvwbjplbgvbhsrlpgdmjqwftvncz"""

puzzle = Puzzle(day=6, year=2022)
or_in = puzzle.input_data
# or_in = ex_in

for i in range(len(or_in) - 3):
    if or_in[i] != or_in[i + 1] and \
            or_in[i] != or_in[i + 2] and \
            or_in[i] != or_in[i + 3] and \
            or_in[i + 1] != or_in[i + 2] and \
            or_in[i + 1] != or_in[i + 3] and \
            or_in[i + 2] != or_in[i + 3]:
        res = i + 4
        break

print(res)
puzzle.answer_a = res
