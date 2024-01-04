def is_valid(idx, seq):
    return 0 <= idx < len(seq)

name = input()
count = 0
data = input()

while data != "Finish":
    split_data = data.split(" ")
    command = split_data[0]
    if command == 'Replace':
        current_chr = split_data[1]
        new_chr = split_data[2]
        name = name.replace(current_chr, new_chr)
        print(name)

    elif command == 'Cut':
        start_idx = int(split_data[1])
        end_idx = int(split_data[2])

        if is_valid(start_idx, name) and is_valid(end_idx, name):
            name = name[:start_idx + 1] + name[(end_idx +2):]
            print(name)

        else:
            print("Invalid indices!")

    elif command == 'Make':
        com2 = split_data[1]
        if com2 == 'Upper':
            name = name.upper()
            print(name)

        elif com2 == 'Lower':
            name = name.lower()
            print(name)

    elif command == 'Check':
        message_check = split_data[1]
        if message_check in name:
            print(f"Message contains {message_check}")
        else:
            print(f"Message doesn't contain {message_check}")
    else:
        idx_1 = int(split_data[1])
        idx_2 = int(split_data[2])
        if is_valid(idx_1, name) and is_valid(idx_2, name):
            for_sum = name[idx_1:idx_2 + 1]
            for ch in for_sum:
                ch = ord(ch)
                count += ch
            print(count)
        else:
            print("Invalid indices!")

    data = input()








#
# def if_idx_valid(idx, seq):
#     return 0 <= idx < len(seq)
#
#
# descrypted_message = input()
# count = 0
#
# while True:
#     line = input()
#     if line == "Finish":
#         break
#     arg = line.split( )
#     command = arg[0]
#     if command == "Replace":
#         current_char = arg[1]
#         new_char = arg[2]
#         descrypted_message = descrypted_message.replace(current_char, new_char)
#         print(descrypted_message)
#     elif command == "Cut":
#         start_idx = int(arg[1])
#         end_idx = int(arg[2])
#         if if_idx_valid(start_idx, descrypted_message) and if_idx_valid(end_idx, descrypted_message):
#             first_part = descrypted_message[:start_idx]
#             second_part = descrypted_message[end_idx + 1:]
#             descrypted_message = first_part + second_part
#             print(descrypted_message)
#         else:
#             print("Invalid indices!")
#     elif command == "Make":
#         message = arg[1]
#         if message == "Upper":
#             descrypted_message = descrypted_message.upper()
#         elif message == "Lower":
#             descrypted_message = descrypted_message.lower()
#         print(descrypted_message)
#     elif command == "Check":
#         string = arg[1]
#         if string in descrypted_message:
#             print(f"Message contains {string}")
#         else:
#             print(f"Message doesn't contain {string}")
#     else:
#         start_index = int(arg[1])
#         end_index = int(arg[2])
#         if if_idx_valid(start_index, descrypted_message) and if_idx_valid(end_index, descrypted_message):
#             word = descrypted_message[start_index:end_index + 1]
#             for ch in word:
#                 ch = ord(ch)
#                 count += ch
#             print(count)
#         else:
#             print("Invalid indices!")