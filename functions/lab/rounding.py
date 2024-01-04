def rounding(num):
    result = []
    for i in num:
        result.append(round(i))

    print(result)


nums = [float(x) for x in input().split()]

rounding(nums)
