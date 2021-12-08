with open("advent_5.txt", "r") as f:
    l = f.read().splitlines()

for i in range(len(l)):
    l[i] = l[i].split()
    l[i] = l[i][0].split(","), l[i][2].split(",")

lines = []
for i in range(len(l)):
    if l[i][0][0] == l[i][1][0] or l[i][0][1] == l[i][1][1]:
        lines.append(l[i])
diagram = []

for i in range(1000):
    row = []
    for j in range(1000):
        row.append(0)
    diagram.append(row)


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
        else:
            line = ([line[1][0], line[0][1]], [line[0][0], line[1][1]])
            return line

    if a == "y":
        if int(line[0][1]) < int(line[1][1]):
            return line
        else:
            line = ([line[0][0], line[1][1]], [line[1][0], line[0][1]])
            return line


def plot(diagram, line):
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


for line in lines:
    diagram = plot(diagram, line)

# print(diagram)

count = 0
for i in range(len(diagram)):
    for j in range(len(diagram[i])):
        if diagram[i][j] > 1:
            count += 1

print(count)
