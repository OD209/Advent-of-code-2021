with open("advent_6.txt", "r") as f:
    f = f.read().splitlines()
f = f[0].split(",")

fish = [int(i) for i in f]

counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]


for i in fish:
    counts[i] += 1

for j in range(256):
    zeros = counts[0]
    for i in range(len(counts)):
        if i != 8:
            counts[i] = counts[i+1]
    counts[8] = zeros
    counts[6] += zeros

count = 0
for i in counts:
    count += i

print(count)
