with open("advent_2.txt", "r") as f:
    ins = f.read().splitlines()

instructions = []
for i in ins:
    instruction = i.split()[0], int(i.split()[1])
    instructions.append(instruction)

vertical = 0
horizontal = 0
for i in instructions:
    if i[0] == "up":
        vertical -= i[1]
    if i[0] == "down":
        vertical += i[1]
    if i[0] == "forward":
        horizontal += i[1]

print(vertical * horizontal)
