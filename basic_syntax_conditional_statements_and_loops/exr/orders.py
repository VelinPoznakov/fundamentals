number_of_orders = int(input())
count_price = 0
for _ in range(1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed = int(input())
    if price_per_capsule > 100 or days > 31 or capsules_needed > 2000 or price_per_capsule < 0.01 or days < 1 or \
            capsules_needed < 1:
        continue
    price_per_coffe = price_per_capsule * days * capsules_needed
    count_price += price_per_coffe
    print(f"The price for the coffee is: ${price_per_coffe:.2f}")
print(f"Total: ${count_price:.2f}")
