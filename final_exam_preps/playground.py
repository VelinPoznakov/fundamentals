import re

n = int(input())

for i in range(n):
    line = input()
    match = re.match(r'^"|[A-Z]{4,}|#([A-Za-z]+ [A-Za-z]+)$', line)
    if match:
        boss_name = match.group(1)
        title = match.group(2)
        print(f"{boss_name}, The {title}\n>> Strength: {len(boss_name)}\n>> Armor: {len(title)}")
    else:
        print("Access denied!")