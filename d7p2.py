from aocd.models import Puzzle

ex_in = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

puzzle = Puzzle(day=7, year=2022)
or_in = puzzle.input_data
#or_in = ex_in


class node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.childs = []
        self.size = 0

    def addChild(self, child):
        i = -1
        for c in self.childs:
            if child.name == c.name:
                i = self.childs.index(c)
                break
        if i == -1:
            self.childs.append(child)
            return self.childs[len(self.childs) - 1]
        else:
            return self.childs[i]

    def getRoot(self):
        while self.parent != None:
            self = self.parent
        return self


i = -1
step_backs = 0
lines = or_in.split("\n")
dirs = node("root", None)
for line in range(len(lines)):
    if "$" in lines[line]:
        if "cd" in lines[line]:
            if "." in lines[line]:
                dirs = dirs.parent
            else:
                dirs = dirs.addChild(node(lines[line].split(" ")[2], dirs))
        elif "ls" in lines[line]:
            line += 1
            while "$" not in lines[line]:
                if "dir" in lines[line]:
                    dirs.addChild(node(lines[line].split(" ")[1], dirs))
                else:
                    dirs.size += int(lines[line].split(" ")[0])
                if line + 1 == len(lines):
                    break
                else:
                    line += 1
            line -= 1
dirs = dirs.getRoot()

table = []


def sum(node, s):
    for child in node.childs:
        s=0
        s = sum(child, s)
        node.size += s
        table.append([child.name, child.size])
    return node.size


sum(dirs, 0)
res = 0
print(table)
to_del = 30000000 - (70000000 - table[len(table)-1][1])
table.sort(key = lambda x: x[1])
print(table)
for node in table:
    if int(node[1]) >= to_del:
        res = int(node[1])
        break
print(res)

puzzle.answer_b = res
