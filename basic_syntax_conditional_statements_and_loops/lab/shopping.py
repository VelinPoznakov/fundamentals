budget = int(input())
price = input()
while price != 'End':
    price1 = int(price)
    budget -= price1
    if budget < 0:
        print('You went in overdraft!')
        exit()
    price = input()
print('You bought everything needed.')