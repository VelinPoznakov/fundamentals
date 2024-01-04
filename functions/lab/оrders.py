def make_order(thing, count):
    if thing == 'coffee':
        coffe = 1.50
        return f'{coffe * count:.2f}'

    elif thing == 'coke':
        coke = 1.40
        return f'{coke * count:.2f}'

    elif thing == 'water':
        water = 1.00
        return f'{water * count:.2f}'

    else:
        snacks = 2.00
        return f'{snacks * count:.2f}'


order = input()
n = int(input())

print(make_order(order, n))
