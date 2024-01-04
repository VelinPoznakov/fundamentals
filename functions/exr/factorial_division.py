# def factorial(fac, devision, res):
#     if num > 0:
#         for i in range(1, fac + 1):
#             res *= i
#
#     print(f"{res / devision:.2f}")
#
#
# num = int(input())
# devisior = int(input())
# result = 1
#
# factorial(num, devisior, result)


def factorial_division(num1, num2):
    fact1 = 1
    for i in range(1, num1 + 1):
        fact1 *= i

    fact2 = 1
    for i in range(1, num2 + 1):
        fact2 *= i

    division = fact1 / fact2
    print("{:.2f}".format(division))


num1 = int(input())
num2 = int(input())

factorial_division(num1, num2)
