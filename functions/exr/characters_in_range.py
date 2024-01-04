import jango
def chra(a, d):
    some = []
    for ch in range(ord(a) + 1, ord(d)):
        some.append(chr(ch))
    return some






character1 = input()
character2 = input()
result = chra(character1, character2)
print(' '.join(result))




