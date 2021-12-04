with open("advent_3.txt", "r") as f:
    nums = f.read().splitlines()

nums1 = nums
c = nums[0]
count = []

for i in c:
    count.append(int(i))

bitNum = len(count)


def num_of_1(lst):
    c = lst[0]
    startCount = []
    for k in c:
        startCount.append(int(k))

    for i in range(1, len(lst)):
        for j in range(len(startCount)):
            current_val = int(startCount[j])
            add_val = int(lst[i][j])
            startCount[j] = str(current_val + add_val)

    return startCount


def shorten(lst, i):
    x = num_of_1(lst)

    if int(x[i]) > len(lst)/2 or int(x[i]) == len(lst)/2:
        y = 1
    else:
        y = 0

    remove_lst = []
    for j in range(len(lst)):
        if int(lst[j][i]) != y:
            remove_lst.append(lst[j])

    n_lst = [num for num in lst if num not in remove_lst]

    return n_lst


def shorten2(lst, i):
    x = num_of_1(lst)
    if int(x[i]) >= len(lst)/2:
        y = 0
    else:
        y = 1

    remove_lst = []
    for j in range(len(lst)):
        if int(lst[j][i]) != y:
            remove_lst.append(lst[j])
    n_lst = [num for num in lst if num not in remove_lst]

    return n_lst


for i in range(bitNum):
    if len(nums) > 1:
        nums = shorten(nums, i)

    if len(nums1) > 1:
        nums1 = shorten2(nums1, i)

print(int(nums[0], 2) * int(nums1[0], 2))
