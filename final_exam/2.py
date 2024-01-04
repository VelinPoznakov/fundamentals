line = input()
heroes = {}


while line != "End":
    line = input()
    arg = line.split(" ")
    command = arg[0]

    if command == "Enroll":
        hero = arg[1]
        if hero not in heroes:
            heroes["hero"] = hero
        else:
            print(f"{hero} is already enrolled.")
    elif command == "Learn":
        hero = arg[1]
        spell = arg[2]
        if spell not in heroes:
            heroes['hero'] = {'spell': spell}
        else:
            print(f"{hero} has already learnt {spell}.")
        if hero not in heroes["hero"]:
            print(f"{hero} doesn't exist.")
    elif command == "Unlearn":
        hero = arg[1]
        spell = arg[2]
        if hero not in heroes["hero"]:
            print(f"{hero} doesn't exist.")
        if spell not in heroes:
            print(f"{hero} doesn't know {spell}.")
        del heroes["spell"]
for hero, spell in heroes.items():
    print("Heroes:")
    print(f"== {heroes[hero]}: {heroes[spell]}")