white_gold = [int(x) for x in input().split()]
yellow_gold = [int(x) for x in input().split()]
lesftover = 0
earings = 0
for x in white_gold:
    t = int(x)
    for w in yellow_gold:
        s = int(w)
        if t + w == 10:
            earings += 1
        if t + s > 10:
            earings += 1
            s -= 2
            if t + s > 10:
                earings += 1
                s -= 2
            if t + s == 10:
                earings += 1
        if t + s < 10:
            lesftover += t + s
        if lesftover > 10:
            earings += 1
            if lesftover > 20:
                earings += 1
if earings >= 7:
    print(f"Great success, you created {earings} earrings.")
else:
    left = 7 - earings
    print(f"Keep trying, you need {left} more earrings.")