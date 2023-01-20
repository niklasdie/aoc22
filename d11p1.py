from aocd.models import Puzzle

ex_in = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

puzzle = Puzzle(day=11, year=2022)
or_in = puzzle.input_data
or_in = ex_in

m = []

for line in or_in.split("\n"):
    line.strip()
    m_i = -1
    if "Monkey" in line:
        m_i += 1
    if "Starting items: " in line:
        m.append([])
        line.replace("Starting items: ", "")
        line.replace(" ", "")
        m[m_i].append(line.split(","))
    if "Operation: " in line:
        if line[line.find("old") + 2] == "*": #21
            if "old" in line[line.find("old") + 3:]:
                for i in m[m_i]:
                    i *= i
            else:
                for i in m[m_i]:
                    i *= line[line.find("old") + 3:]
        if line[line.find("old") + 2] == "+": #21
            if "old" in line[line.find("old") + 3:]:
                for i in m[m_i]:
                    i += i
            else:
                for i in m[m_i]:
                    i += line[line.find("old") + 3:]
    if ""

#puzzle.answer_a = res
