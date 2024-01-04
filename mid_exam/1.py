jorney = float(input())
months = int(input())
money = 0

for monat in range(1, months + 1):

    if monat % 2 != 0 and monat > 1:
        money -= (money * 0.16)

    if monat % 4 == 0:
        money += (money * 0.25)
    money += jorney * 0.25


a = abs(money - jorney)
if money >= jorney:
    print(f"Bravo! You can go to Disneyland and you will have {a:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {a:.2f}lv. more.")