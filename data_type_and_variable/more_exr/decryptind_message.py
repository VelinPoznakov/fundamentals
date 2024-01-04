key = int(input())
itr = int(input())
message = []
for i in range(1, itr + 1):
    letter = input()

    num = ord(letter)
    final = chr(num + key)
    message.append(final)

print(''.join(message))


