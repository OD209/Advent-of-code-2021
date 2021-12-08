with open("advent_7.txt", "r") as f:
    c = f.read().splitlines()
c = c[0].split(",")

crabs = [int(i) for i in c]

top = 0
for i in crabs:
    if i > top:
        top = i

lowest_cost = 99999999
for i in range(top):
    total_fuel_cost = 0
    for j in crabs:
        fuel_cost = abs(i-j)
        total_fuel_cost += fuel_cost

    if total_fuel_cost < lowest_cost:
        lowest_cost = total_fuel_cost

print(lowest_cost)
