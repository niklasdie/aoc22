import aocd

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
    or_in = aocd.get_data(day=1, year=2022)
    in_arr = or_in.split("\n")
    sum_list = []
    last_i = 0
    for i in range(len(in_arr)):
        if in_arr[i] == "":
            sum_list.append(sum(int(in_arr[x]) for x in range(last_i, i)))
            last_i = i+1
    s = 0
    for i in range(3):
        s += int(max(sum_list))
        sum_list.remove(max(sum_list))
    aocd.submit(answer=s, part="b", day=1, year=2022)
