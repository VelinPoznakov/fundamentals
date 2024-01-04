def even_odd(n):
    counter_even = 0
    counter_odd = 0
    for ch in n:
        number = int(ch)
        if number % 2 == 0:
            counter_even += number
        else:
            counter_odd += number
    return f"Odd sum = {counter_odd}, Even sum = {counter_even}"

num = input()
print(even_odd(num))

