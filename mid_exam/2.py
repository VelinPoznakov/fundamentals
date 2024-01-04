num = [int(x) for x in input().split()]
index = 0
new = []
f = []
while True:
    command = input().split()
    if command[0] == 'add':
        for i in command:
            if i.isdigit():

                digit = int(i)
                num.insert(index, digit)
                index += 1
    elif command[0] == "remove":
        if command[1] == 'greater':
            value = int(command[3])
            for n in num:
                if value < n:
                    num.remove(n)
            for n in num:
                if value < n:
                    num.remove(n)
        elif command[1] == "at":
            index = int(command[3])
            if 0 <= index <= len(num):
                num.pop(index)
    elif command[0] == "replace":
        num1 = int(command[1])
        num2 = int(command[2])
        if num1 in num:
            if num1 in num:
                idx = num.index(num1)
                num[idx] = num2
    elif command[0] == 'find':
        if command[1] == "even":
            for n in num:
                if n % 2 == 0:
                    new.append(str(n))
            print(' '.join(new))
        elif command[1] == "odd":
            for n in num:
                if n % 2 != 0:
                    f.append(str(n))
            print(' '.join(f))
    elif command[0] == 'END':
        break

print(*num, sep=', ')
