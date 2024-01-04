message = input()

data = input()

while data != 'Decode':

    splited_data = data.split('|')
    command = splited_data[0]
    if command == 'Move':
        n = int(splited_data[1])
        first = message[:n]
        second = message[n:]
        message = second + first
    elif command == 'Insert':
        index = int(splited_data[1])
        strin_given = splited_data[2]
        message = message[:index] + strin_given + message[index:]
    elif command == 'ChangeAll':
        change = splited_data[1]
        some = splited_data[2]
        message = message.replace(change, some)



    data = input()

print(f'The decrypted message is: {message}')









