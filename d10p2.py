from aocd.models import Puzzle

ex_in = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

puzzle = Puzzle(day=10, year=2022)
or_in = puzzle.input_data
#or_in = ex_in


def part_a(input):
    X = 1
    cycle = 0
    cycles_to_check = [20 + (40 * i) for i in range(6)]
    signal_strength = 0
    for line in input.split("\n"):
        if len(line.split()) == 2:
            instruction, V = line.split()
            V = int(V)
        else:
            cycle += 1
            if cycle in cycles_to_check:
                signal_strength += (cycle * X)
            continue
        for i in range(2):
            cycle += 1
            if i == 1:
                if cycle in cycles_to_check:
                    signal_strength += (cycle * X)
                X += V
            else:
                if cycle in cycles_to_check:
                    signal_strength += (cycle * X)
    return signal_strength


def part_b(input):
    X = 1
    V_list = []
    for line in input.split("\n"):
        if len(line.split()) == 1:
            V_list.append(X)
        else:
            V = int(line.split()[1])
            V_list.append(X)
            V_list.append(X)
            X += V
    for row in range(0, len(V_list), 40):
        for col in range(40):
            print(end='##' if abs(V_list[row + col] - col) <= 1 else '..')
        print()
    return 'REHPRLUB'

part_b(or_in)
# puzzle.answer_b = res
