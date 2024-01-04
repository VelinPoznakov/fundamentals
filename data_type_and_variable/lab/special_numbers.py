n = int(input())
for i in range(1, n + 1):
    is_true = False
    if i == 5 or i == 7 or i == 11:
        is_true = False
    num_is_str = str(i)
    sum_di = 0
    for ch in num_is_str:
        sum_di += int(ch)
    if sum_di == 5 or sum_di == 7 or sum_di == 11:
        is_true = True
    print(f'{i} -> {is_true}')
