nums = [int(x) for x in input().split(", ")]
for i in nums:
    if i == 0:
        nums.remove(i)
        nums.append(i)

print(nums)
