with open("advent_6.txt", "r") as f:
    f = f.read().splitlines()
f = f[0].split(",")
fish = []
for i in f:
    fish.append(int(i))

for j in range(80):
    new_fish = []
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            new_fish.append(8)
        else:
            fish[i] -= 1
    if len(new_fish) > 0:
        fish = fish + new_fish

print(len(fish))
