with open("advent_5.txt", "r") as f:
    l = f.read().splitlines()

for i in range(len(l)):
    l[i] = l[i].split()
    l[i] = l[i][0].split(","), l[i][2].split(",")

lines = l
diagram = []

for i in range(1000):
    row = []
    for j in range(1000):
        row.append(0)
    diagram.append(row)


def check_diagonal(line):
    if line[0][0] == line[1][0]:
        return False
    elif line[0][1] == line[1][1]:
        return False
    else:
        return True


def find_axis(line):
    if line[0][0] == line[1][0]:
        return "y"
    elif line[0][1] == line[1][1]:
        return "x"


def order_line(line):
    a = find_axis(line)
    if a == "x":
        if int(line[0][0]) < int(line[1][0]):
            return line
        elif int(line[0][0]) > int(line[1][0]):
            line = ([line[1][0], line[0][1]], [line[0][0], line[1][1]])
            return line

    if a == "y":
        if int(line[0][1]) < int(line[1][1]):
            return line
        elif int(line[0][1]) > int(line[1][1]):
            line = ([line[0][0], line[1][1]], [line[1][0], line[0][1]])
            return line


def diagonal_direction(line):
    if int(line[0][1]) > int(line[1][1]):
        if int(line[0][0]) > int(line[1][0]):
            return "up left"
        elif int(line[0][0]) < int(line[1][0]):
            return "up right"
    elif int(line[0][1]) < int(line[1][1]):
        if int(line[0][0]) > int(line[1][0]):
            return "down left"
        elif int(line[0][1]) < int(line[1][1]):
            return "down right"


def plot(diagram, line):
    if check_diagonal(line) == False:
        line = order_line(line)
        axis = find_axis(line)
        if axis == "y":
            y = int(line[0][0])
            for x in range(int(line[0][1]), int(line[1][1])+1):
                #print("x", x, "y", y)
                diagram[x][y] += 1
            return diagram
        elif axis == "x":
            x = int(line[0][1])
            for y in range(int(line[0][0]), int(line[1][0])+1):
                #print("x", x, "y", y)
                diagram[x][y] += 1
            return diagram
    else:
        if diagonal_direction(line) == "up right":
            x = int(line[0][0])
            y = int(line[0][1])
            while x <= int(line[1][0]):
                diagram[y][x] += 1
                x += 1
                y -= 1
            return diagram

        elif diagonal_direction(line) == "up left":
            x = int(line[0][0])
            y = int(line[0][1])
            while x >= int(line[1][0]):
                diagram[y][x] += 1
                x -= 1
                y -= 1
            return diagram

        elif diagonal_direction(line) == "down right":
            x = int(line[0][0])
            y = int(line[0][1])
            while x <= int(line[1][0]):
                diagram[y][x] += 1
                x += 1
                y += 1
            return diagram

        elif diagonal_direction(line) == "down left":
            x = int(line[0][0])
            y = int(line[0][1])
            while x >= int(line[1][0]):
                diagram[y][x] += 1
                x -= 1
                y += 1
            return diagram


for line in lines:
    diagram = plot(diagram, line)

count = 0
for i in range(len(diagram)):
    for j in range(len(diagram[i])):
        if diagram[i][j] > 1:
            count += 1

print(count)
