from aocd.models import Puzzle

ex_in = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

puzzle = Puzzle(day=9, year=2022)
or_in = puzzle.input_data
# or_in = ex_in

def move(h, t, d):
    if d == "R" or d == "L":
        if h[1] != t[1] and abs(h[0] - t[0]) > 1:
            t[1] = h[1]
        if abs(h[0] - t[0]) > 1:
            if d == "R":
                t[0] += 1
            else:
                t[0] -= 1
            return True
    if d == "U" or d == "D":
        if h[0] != t[0] and abs(h[1] - t[1]) > 1:
            t[0] = h[0]
        if abs(h[1] - t[1]) > 1:
            if d == "U":
                t[1] += 1
            else:
                t[1] -= 1
            return True
    return False


h_coords = [0, 0]
t_coords = [0, 0]
visited = []
for line in or_in.split("\n"):
    if "R" in line:
        for i in range(int(line.split(" ")[1])):
            h_coords[0] += 1
            if move(h_coords, t_coords, "R"):
                visited.append(t_coords[:])
    if "L" in line:
        for i in range(int(line.split(" ")[1])):
            h_coords[0] -= 1
            if move(h_coords, t_coords, "L"):
                visited.append(t_coords[:])
    if "U" in line:
        for i in range(int(line.split(" ")[1])):
            h_coords[1] += 1
            if move(h_coords, t_coords, "U"):
                visited.append(t_coords[:])
    if "D" in line:
        for i in range(int(line.split(" ")[1])):
            h_coords[1] -= 1
            if move(h_coords, t_coords, "D"):
                visited.append(t_coords[:])
print(visited)
visited = set(map(tuple, visited))
print(visited)
res = len(visited) + 1
print(res)
# puzzle.answer_a = res
