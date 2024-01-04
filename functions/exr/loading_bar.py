import math


def resurlt(num):
    # num = 100
    new = math.ceil(num / 10)
    # new = 10
    if new == 10:
        print(f"{new}0% Complete!")
        return print(f"[{'%' * new}]")
    else:
        s1 = '%' * new
        s2 = '.' * (10 - len(s1))
        print(f"{new}0% [{s1 + s2}]")
        return print("Still loading...")


num = int(input())
# 100 / 10
resurlt(num)
