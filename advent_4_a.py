with open("advent_4.txt", "r") as f:
    data = f.read().splitlines()

nums = data[0].split(",")

tables = []
table = []
for i in range(2, len(data)):
    if data[i] == "":
        tables.append(table)
        table = []
    else:
        table.append(data[i].split())

tables.append(table)


def check_bingo(lst):
    for i in lst:
        if "*" not in i:
            return False
    return True


def create_column(lst):
    nlst = []
    column = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            # print(lst[j][i])
            column.append(lst[j][i])

        nlst.append(column)
        column = []
    return(nlst)


def bingo(lst):
    for i in lst:
        if check_bingo(lst):
            return True
    return False


def update_lst(lst, num):
    for i in range(len(lst)):
        # print(lst[i], num)
        if lst[i] == num:
            lst[i] += "*"
        # print(lst)
    return(lst)


def run(nums, tables):
    # print(tables1)
    for number in range(len(nums)):
        for i in range(len(tables)):
            # print(tables[i])
            for j in range(len(tables[i])):
                og_table = tables[i][j]
                tables[i][j] = update_lst(tables[i][j], nums[number])

                # print(tables[i])
                if bingo(tables[i][j]):
                    win = tables[i][j]
                    win_table = tables[i]
                    return win, nums[number], win_table

            # columns

                # print(tables[i])
                c_tables = []
                for k in range(len(tables)):
                    c_tables.append(create_column(tables[k]))

                tables[i][j] = update_lst(c_tables[i][j], nums[number])

                if bingo(tables[i][j]):
                    win = tables[i][j]
                    win_table = c_tables[i]
                    return win, nums[number], win_table

                tables[i][j] = og_table


x = run(nums, tables)
print(x)
count = 0
for i in range(len(x[2])):
    for j in range(len(x[2][i])):
        if "*" not in x[2][i][j]:
            count += int(x[2][i][j])

print(count)
print(count*int(x[1]))
