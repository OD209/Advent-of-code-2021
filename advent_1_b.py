with open("advent_1.txt", "r") as f:
    d = f.read().splitlines()

depth = [int(i) for i in d]

threes = []
for i in range(len(depth)-2):
    value = depth[i] + depth[i+1] + depth[i+2]
    threes.append(value)

count = 0
for i in range(len(threes)-1):
    if threes[i] < threes[i+1]:
        count += 1

print(count)
