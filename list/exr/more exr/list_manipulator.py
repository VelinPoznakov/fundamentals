def is_valid_index(idx, seq):
    return 0 <= idx < len(seq)

nums = [int(x) for x in input().split()]
line = input()
count = 0
min_n = []
max_n = []
first = []
last = []

while line != 'end':
    command_ark = line.split()
    command = command_ark[0]
    if command == 'exchange':
        next_com = int(command_ark[1])
        if is_valid_index(next_com, nums):
            for i in nums:
                count += 1
                if count < next_com + 1:
                    nums.remove(i)
                    nums.append(i)
        else:
            print("Invalid index")

    elif command == 'max':
        next_com = command_ark[1]
        if next_com == 'even':
            for num in nums:
                if num % 2 == 0:
                    if num > count:
                        count = num
            print(count)
        else:
            for num in nums:
                if num % 2 != 0:
                    if num > count:
                        count = num
            print(count)

    elif command == 'min':
        next_com = command_ark[1]
        con = 99999999999999
        if next_com == "even":
            for num in nums:
                if num % 2 == 0:
                    if num < con:
                        con = num
                        min_n.append(num)
#            print(min_n.index(min(min_n)))

        else:
            for num in nums:
                if num % 2 == 0:
                    min_n. append(num)
            print(min_n.index(min(min_n)))

    elif command == 'first':
        next_com = command_ark[2]
        w = int(command_ark[1])
        if next_com == 'even':
            for num in nums:
                if num % 2 == 0:
                    count += 1
                    first.append(num)
                    if count == w:
                        print(first)

        else:
            for num in nums:
                if num % 2 != 0:
                    count += 1
                    first.append(num)
                    if count == w:
                        print(first)

    elif command == 'last':
        next_com = command_ark[2]
        w = int(command_ark[1])
        if next_com == 'even':
            for num in nums:
                if num % 2 == 0:
                    count += 1
                    last.append(num)
                    if count == w:
                        print(last)

        else:
            for num in nums:
                if num % 2 != 0:
                    count += 1
                    last.append(num)
                    if count == w:
                        print(last)

    line = input()