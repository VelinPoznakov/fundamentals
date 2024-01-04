nums = [int(x) for x in input().split()]
line = input()

while line != 'END':

    commans = line.split()
    command = commans[0]

    if command == 'Change':
        num = int(commans[1])
        new_num = int(commans[2])
        if num in nums:
            idx1 = nums.index(num)
            nums[idx1] = new_num
    elif command == 'Hide':
        num = int(commans[1])
        if num in nums:
            nums.remove(num)

    elif command == 'Switch':
        num1 = int(commans[1])
        num2 = int(commans[2])
        if num1 in nums and num2 in nums:
            idx1 = nums.index(num1)
            idx2 = nums.index(num2)
            nums[idx1] = num2
            nums[idx2] = num1

    elif command == 'Insert':
        idx = int(commans[1])
        num = int(commans[2])
        if 0 <= idx < len(nums):
            nums.insert(idx + 1, num)

    else:
        nums.reverse()
    line = input()

print(*nums, sep=' ')
