import aocd
from aocd.models import Puzzle

ex_in = """A Y
B X
C Z"""

rock = 1
paper = 2
scissors = 3
draw = 3
win = 6

puzzle = Puzzle(day=2, year=2022)
or_in = puzzle.input_data
#or_in = ex_in
max = sum = 0
for x in or_in.split("\n"):
    if x[2] == "X":
        sum += rock
        if x[0] == "A":
            sum += draw
        elif x[0] == "C":
            sum += win
    if x[2] == "Y":
        sum += paper
        if x[0] == "B":
            sum += draw
        elif x[0] == "A":
            sum += win
    if x[2] == "Z":
        sum += scissors
        if x[0] == "C":
            sum += draw
        elif x[0] == "B":
            sum += win
    if max < sum:
        max = sum
print(max)
puzzle.answer_a = max
