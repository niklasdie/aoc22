from aocd.models import Puzzle

ex_in = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

if __name__ == '__main__':
    # variant with Puzzle
    puzzle = Puzzle(year=2022, day=1)
    or_in = puzzle.input_data
    in_arr = or_in.split("\n")
    sum_list = []
    last_i = 0
    for i in range(len(in_arr)):
        if in_arr[i] == "":
            sum_list.append(sum(int(in_arr[x]) for x in range(last_i, i)))
            last_i = i+1
    puzzle.answer_a = max(sum_list)

