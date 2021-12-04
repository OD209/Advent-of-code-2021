with open("advent_3.txt", "r") as f:
    nums = f.read().splitlines()

c = nums[0]
count = []
for i in c:
    count.append(int(i))

for i in range(1, len(nums)):
    for j in range(len(count)):
        c = int(count[j])
        n = int(nums[i][j])
        count[j] = str(c+n)

gamma_rate = ""
epsilon_rate = ""

for i in count:
    if int(i) > (len(nums)/2):
        gamma_rate += "1"
    else:
        gamma_rate += "0"

for i in count:
    if int(i) > (len(nums)/2):
        epsilon_rate += "0"
    else:
        epsilon_rate += "1"

print(int(gamma_rate, 2) * int(epsilon_rate, 2))
