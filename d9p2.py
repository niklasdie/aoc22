from aocd.models import Puzzle
import numpy as np

ex_in = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

puzzle = Puzzle(day=9, year=2022)
or_in = puzzle.input_data
#or_in = ex_in


def shift(h, t, d):
    if d == "R" or d == "L":
        if abs(h[0] - t[0]) > 1:
            t[1] = h[1]
            return True
    if d == "U" or d == "D":
        if abs(h[1] - t[1]) > 1:
            t[0] = h[0]
            return True
    return False


def move(h, t, d):
    if abs(h[0] - t[0]) > 1:
        t[0] += np.sign(h[0] - t[0])
        if abs(h[0] - t[0]) != 0:
            t[1] += np.sign(h[1] - t[1])
            return True
    if abs(h[1] - t[1]) > 1:
        t[1] += np.sign(h[1] - t[1])
        if abs(h[1] - t[1]) != 0:
            t[0] += np.sign(h[0] - t[0])
            return True
    return False

t_coords = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
visited = []
for line in or_in.split("\n"):
    if "R" in line:
        for i in range(int(line.split(" ")[1])):
            t_coords[0][0] += 1
            for r in range(1, len(t_coords)):
                if move(t_coords[r - 1], t_coords[r], "R") and r == 9:
                    visited.append(t_coords[r][:])
    if "L" in line:
        for i in range(int(line.split(" ")[1])):
            t_coords[0][0] -= 1
            for r in range(1, len(t_coords)):
                if move(t_coords[r - 1], t_coords[r], "L") and r == 9:
                    visited.append(t_coords[r][:])
    if "U" in line:
        for i in range(int(line.split(" ")[1])):
            t_coords[0][1] += 1
            for r in range(1, len(t_coords)):
                if move(t_coords[r - 1], t_coords[r], "U") and r == 9:
                    visited.append(t_coords[r][:])
    if "D" in line:
        for i in range(int(line.split(" ")[1])):
            t_coords[0][1] -= 1
            for r in range(1, len(t_coords)):
                if move(t_coords[r - 1], t_coords[r], "D") and r == 9:
                    visited.append(t_coords[r][:])
    print(t_coords)
    print("=========================================================================================")
print(visited)
visited = set(map(tuple, visited))
print(visited)
res = len(visited) + 1
print(res)
puzzle.answer_b = res
