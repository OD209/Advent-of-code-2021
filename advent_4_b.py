with open("advent_4.txt", "r") as f:
    data = f.read().splitlines()


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
        if lst[i] == num:
            lst[i] += "*"
    return(lst)


def run(nums, tables):
    for number in range(len(nums)):
        for i in range(len(tables)):
            for j in range(len(tables[i])):
                og_table = tables[i][j]
                tables[i][j] = update_lst(tables[i][j], nums[number])

                if bingo(tables[i][j]):
                    tables.pop(i)

                c_tables = []
                for k in range(len(tables)):
                    c_tables.append(create_column(tables[k]))

                tables[i][j] = update_lst(c_tables[i][j], nums[number])

                if bingo(tables[i][j]):
                    tables.pop(i)

                tables[i][j] = og_table


def update_columns(c_table, num):
    updated_c = []
    for i in range(len(c_table)):
        updated_c.append(update_lst(c_table[i], nums[num]))
    return updated_c


def update_rows(table, num):
    updated_t = []
    for i in range(len(table)):
        updated_t.append(update_lst(table[i], nums[num]))
    return updated_t


def find_last(nums, tables, column_tables):
    winners = []

    for number in range(len(nums)):
        for i in range(len(tables)):
            
            if tables[i] not in winners and column_tables[i] not in winners:
                for j in range(len(tables[i])):
                    # all rows / columns
                    initial_row = tables[i][j]
                    initial_column = column_tables[i][j]

                    # rows, row = tables[i][j]
                    tables[i][j] = update_lst(tables[i][j], nums[number])
                    column_tables[i][j] = update_lst(
                        column_tables[i][j], nums[number])

                    if check_bingo(tables[i][j]):
                        winners.append(tables[i])
                        if len(winners) == len(tables):
                            return(winners[len(winners)-1], nums[number])
                        break
                    elif check_bingo(column_tables[i][j]):
                        winners.append(column_tables[i])
                        if len(winners) == len(tables):
                            return(winners[len(winners)-1], nums[number])
                        break

                    tables[i][j] = initial_row
                    column_tables[i][j] = initial_column


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

column_tables = []
for i in range(len(tables)):
    column_tables.append(create_column(tables[i]))

x = find_last(nums, tables, column_tables)

count = 0
for i in range(len(x[0])):
    for j in range(len(x[0][i])):
        if "*" not in x[0][i][j]:
            count += int(x[0][i][j])

print(count, x[1], count*int(x[1]))

# print(tables)
