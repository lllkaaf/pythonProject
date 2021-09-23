nums = [3, 7, -12, 22, 9, 10, 1, 3, 33, 44, 33, 6, -18, 22]
x = sorted(nums)

for i in x:
    if i <= 10:
        nums.remove(i)


print(nums)


