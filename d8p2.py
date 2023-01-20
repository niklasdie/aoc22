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
for y in range(len(trees)):
    for x in range(len(trees[y])):
        if y != 0 and y != len(trees) - 1 and x != 0 and x != len(trees[y]) - 1:
            distance_x1 = 0
            stop = 0
            for dx in range(x-1, -1, -1):
                if trees[y][x] > trees[y][dx] and stop == 0:
                    distance_x1 += 1
                elif trees[y][x] <= trees[y][dx] and stop == 0:
                    distance_x1 += 1
                    stop = 1
                else:
                    stop = 1
            distance_x2 = 0
            stop = 0
            for dx in range(x + 1, len(trees[y])):
                if trees[y][x] > trees[y][dx] and stop == 0:
                    distance_x2 += 1
                elif trees[y][x] <= trees[y][dx] and stop == 0:
                    distance_x2 += 1
                    stop = 1
                else:
                    stop = 1
            distance_y1 = 0
            stop = 0
            for dy in range(y-1, -1, -1):
                if trees[y][x] > trees[dy][x] and stop == 0:
                    distance_y1 += 1
                elif trees[y][x] <= trees[dy][x] and stop == 0:
                    distance_y1 += 1
                    stop = 1
                else:
                    stop = 1
            distance_y2 = 0
            stop = 0
            for dy in range(y + 1, len(trees[y])):
                if trees[y][x] > trees[dy][x] and stop == 0:
                    distance_y2 += 1
                elif trees[y][x] <= trees[dy][x] and stop == 0:
                    distance_y2 += 1
                    stop = 1
                else:
                    stop = 1
            if res < distance_x1 * distance_x2 * distance_y1 * distance_y2:
                res = distance_x1 * distance_x2 * distance_y1 * distance_y2


print(res)
puzzle.answer_b = res
