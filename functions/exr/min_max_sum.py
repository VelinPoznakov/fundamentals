def mini(x):
    return min(x)


def maxi(x):
    return max(x)


def sum_all(x):
    counter = 0
    for num in x:
        counter += num
    return counter


x = [int(x) for x in input().split()]
print(f'The minimum number is {mini(x)}')
print(f"The maximum number is {maxi(x)}")
print(f"The sum number is: {sum_all(x)}")