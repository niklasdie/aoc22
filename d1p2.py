import aocd

# variant with get_data and submit
or_in = aocd.get_data(day=1, year=2022)
in_arr = or_in.split("\n")
sum_list = []
last_i = 0
for i in range(len(in_arr)):
    if in_arr[i] == "":
        sum_list.append(sum(int(in_arr[x]) for x in range(last_i, i)))
        last_i = i+1
res = sum(sorted(sum_list)[-3:])
aocd.submit(answer=res, part="b", day=1, year=2022)
