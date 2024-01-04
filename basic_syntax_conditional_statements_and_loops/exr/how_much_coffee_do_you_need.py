
coffee = 0
while True:
    word = input()
    if word == 'END':
        print(coffee)
        break
    if word == 'coding' or word == 'dog' or word == 'cat' or word == 'movie':
        coffee += 1
    elif word == 'CODING' or word == 'DOG' or word == 'CAT' or word == 'MOVIE':
        coffee += 2
    if coffee > 5:
        print("You need extra sleep")
        exit()
