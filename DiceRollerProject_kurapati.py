import random

def num_input():
    num = int(input("Enter how many dice to roll: "))
    return num

def diceRoller(num):
    total = 0
    str_dice_roll = ""
    for x in range(0, num):
        dice_roll = random.randint(1, 6)
        total += dice_roll
        str_dice_roll += str(dice_roll)
    diceCreator(str_dice_roll, total)

def diceCreator(roll, total):
    top = ""
    top_mid = ""
    mid = ""
    bottom_mid = ""
    bottom = ""
    for x in roll:
        for i in x:
            if i == "1":
                top += "- - - - - -\t"
                top_mid += "|         |\t"
                mid += "|    O    |\t"
                bottom_mid += "|         |\t"
                bottom += "- - - - - -\t"
            elif i == "2":
                top += "- - - - - -\t"
                top_mid += "|    O    |\t"
                mid += "|         |\t"
                bottom_mid += "|    O    |\t"
                bottom += "- - - - - -\t"
            elif i == "3":
                top += "- - - - - -\t"
                top_mid += "|    O    |\t"
                mid += "|    O    |\t"
                bottom_mid += "|    O    |\t"
                bottom += "- - - - - -\t"
            elif i == "4":
                top += "- - - - - -\t"
                top_mid += "|  O   O  |\t"
                mid += "|         |\t"
                bottom_mid += "|  O   O  |\t"
                bottom += "- - - - - -\t"
            elif i == "5":
                top += "- - - - - -\t"
                top_mid += "|  O   O  |\t"
                mid += "|    O    |\t"
                bottom_mid += "|  O   O  |\t"
                bottom += "- - - - - -\t"
            elif i == "6":
                top += "- - - - - -\t"
                top_mid += "|  O   O  |\t"
                mid += "|  O   O  |\t"
                bottom_mid += "|  O   O  |\t"
                bottom += "- - - - - -\t"

    mid += "Your score is: "
    mid += str(total)

    print(top)
    print(top_mid)
    print(mid)
    print(bottom_mid)
    print(bottom)

diceRoller(num_input())