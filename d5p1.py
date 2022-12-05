from aocd.models import Puzzle

ex_in = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

puzzle = Puzzle(day=5, year=2022)
or_in = puzzle.input_data
#or_in = ex_in

ship = []
moves = []
i_ship = i_moves = 0
for line in or_in.split("\n"):
    if line != "":
        if line[1] != "1" and line[0] != "m":
            ship.append([])
            for x in range(int((len(line)/4)+1)):
                ship[i_ship].append(line[x * 4 + 1])
            i_ship += 1
        else:
            if line[0] != " ":
                split = line.split(" ")
                moves.append([int(split[1]), int(split[3]), int(split[5])])
                i_moves += 1
print(ship)

ship2 = []
for y in range(len(ship[0])):
    ship2.append([])
for y in range(len(ship)):
    for x in range(len(ship[y])):
        if ship[y][x] != " ":
            ship2[x].append(ship[y][x])
for x in ship2:
    x = x.reverse()
ship = ship2
print(ship)

for move in moves:
    print(move)
    for i in range(move[0]):
        ship[move[2]-1].append(ship[move[1]-1].pop())

print(ship)
res = ""
for x in ship:
    res += x.pop()

print(res)
puzzle.answer_a = res
