def main(com, num_1, num_2):
    if com == 'multiply':
        return num_1 * num_2

    elif com == 'divide':
        return int(num_1 / num_2)

    elif com == 'add':
        return num_1 + num_2

    else:
        return num_1 - num_2


command = input()

num1 = int(input())
num2 = int(input())

print(main(command, num1, num2))
