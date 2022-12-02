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
        #sum += lose
        if x[0] == "A":
            sum += scissors
        elif x[0] == "C":
            sum += paper
        elif x[0] == "B":
            sum += rock
    if x[2] == "Y":
        sum += draw
        if x[0] == "B":
            sum += paper
        elif x[0] == "A":
            sum += rock
        elif x[0] == "C":
            sum += scissors
    if x[2] == "Z":
        sum += win
        if x[0] == "C":
            sum += rock
        elif x[0] == "B":
            sum += scissors
        elif x[0] == "A":
            sum += paper
    if max < sum:
        max = sum
print(max)
puzzle.answer_b = max
