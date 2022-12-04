from aocd.models import Puzzle

ex_in = """2-4,6-8
2-3,4-5
5-7,7-9 
2-8,3-7
6-6,4-6
2-6,4-8"""

puzzle = Puzzle(day=4, year=2022)
or_in = puzzle.input_data
#or_in = ex_in
res = 0
for line in or_in.split("\n"):
    split = line.split(",")
    a = split[0].split("-")
    b = split[1].split("-")
    if int(a[0]) <= int(b[1]) and int(a[1]) >= int(b[0]) or \
            int(a[0]) >= int(b[1]) and int(a[1]) <= int(b[0]):
        res += 1
print(res)
puzzle.answer_b = res
