with open("advent_1.txt", "r") as f:
    d = f.read().splitlines()

depth = [int(i) for i in d]

count = 0
for i in range(len(depth)-1):
    if depth[i] < depth[i+1]:
        count += 1

print(count)
