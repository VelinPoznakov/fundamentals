info = input()

cities = {}

while info != 'Sail':

    splited_info = info.split('||')
    city = splited_info[0]
    population = int(splited_info[1])
    gold = int(splited_info[2])

    if city not in cities:
        cities[city] = {'population': population, 'gold': gold}
    else:
        cities[city]['population'] += population
        cities[city]['gold'] += gold

    info = input()

info = input()

while info != 'End':

    split_info = info.split('=>')
    command = split_info[0]
    if command == 'Plunder':
        city = split_info[1]
        population = int(split_info[2])
        gold = int(split_info[3])
        cities[city]['population'] -= population
        cities[city]['gold'] -= gold
        print(f'{city} plundered! {gold} gold stolen, {population} citizens killed.')
        if cities[city]['gold'] <= 0 or cities[city]['population'] <= 0:
            del cities[city]
            print(f"{city} has been wiped off the map!")
    elif command == 'Prosper':
        city = split_info[1]
        gold = int(split_info[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            info = input()
            continue
        else:
            cities[city]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")

    info = input()

if not cities:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")

    for city, values in cities.items():
        print(f"{city} -> Population: {cities[city]['population']} citizens, Gold: {cities[city]['gold']} kg")
