from aocd.models import Puzzle

ex_in = """30373
25512
65332
33549
35390"""

puzzle = Puzzle(day=8, year=2022)
or_in = puzzle.input_data
#or_in = ex_in

trees = []
for line in or_in.split("\n"):
    t = []
    for x in line:
        t.append(int(x))
    trees.append(t)

res = 0
visible = 0
for y in range(len(trees)):
    for x in range(len(trees[y])):
        if y != 0 and y != len(trees)-1 and x != 0 and x != len(trees[y])-1:
            max = 0
            visible = 0
            for dx in range(x):
                if max < trees[y][dx]:
                    max = trees[y][dx]
            if max < trees[y][x]:
                res += 1
                visible = 1
            max = 0
            if visible == 0:
                for dx in range(x+1, len(trees[y])):
                    if max < trees[y][dx]:
                        max = trees[y][dx]
                if max < trees[y][x]:
                    res += 1
                    visible = 1
                max = 0
            if visible == 0:
                for dy in range(y):
                    if max < trees[dy][x]:
                        max = trees[dy][x]
                if max < trees[y][x]:
                    res += 1
                    visible = 1
                max = 0
            if visible == 0:
                for dy in range(y+1, len(trees[y])):
                    if max < trees[dy][x]:
                        max = trees[dy][x]
                if max < trees[y][x]:
                    res += 1

print(res)
res += 2*len(trees) + 2*len(trees[0]) - 4
print(res)
puzzle.answer_a = res
