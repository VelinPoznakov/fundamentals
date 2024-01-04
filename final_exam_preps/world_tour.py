travels = input()

data = input()

while data != "Travel":
    split_data = data.split(':')
    command = split_data[0]
    if command == "Add Stop":
        idex = int(split_data[1])
        destinnation = split_data[2]
        travels = travels[:idex] + destinnation + travels[idex:]
    elif command == "Remove Stop":
        inex1 = int(split_data[1])
        idex2 = int(split_data[2])
        travels = travels[:inex1] + travels[idex2 +1:]
    else:
        old_dis = split_data[1]
        new_dis = split_data[2]
        travels = travels.replace(old_dis, new_dis)
    print(travels)

    data = input()


print(f"Ready for world tour! Planned stops: {travels}")