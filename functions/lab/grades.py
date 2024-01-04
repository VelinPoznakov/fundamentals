def result(num):
    if 2 <= num <= 2.99:
        print('Fail')

    elif 3 <= num <= 3.59:
        print('Poor')

    elif 3.50 <= num <= 4.49:
        print('Good')

    elif 4.50 <= num <= 5.49:
        print('Very Good')

    else:
        print('Excellent')


grade = float(input())
result(grade)
