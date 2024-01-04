n = int(input())

car_data = {}

for _ in range(n):
    data = input().split('|')
    car = data[0]
    mileage = int(data[1])
    fuel = int(data[2])

    car_data[car] = {'mileage': mileage, 'fuel': fuel}

while True:
    line = input()
    if line == 'Stop':
        break

    split_line = line.split(':')
    command = split_line[0]

    if command == 'Drive ':
        car = split_line[1]
        distance = int(split_line[2])
        fuel = int(split_line[3])
        a = int(car_data[car]['fuel'])
        if fuel > a:
            print("Not enough fuel to make that ride")
        else:
            car_data[car]['mileage'] += distance
            car_data[car]['fuel'] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")


