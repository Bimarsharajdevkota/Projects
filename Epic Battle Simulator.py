import random, os, time

def rollDice(side):
    result = random.randint(1, side)
    return result

def health():
    healthStat = ((rollDice(6) * rollDice(12)) / 2) 
    return healthStat

def strength():
    strengthStat = ((rollDice(6) * rollDice(8)) / 2) 
    return strengthStat

while True:
    print("⚔️ CHARACTER BUILDER ⚔️")
    print()
    name1 = input("Name your Hero 1:\n")
    type1 = input("Character Type (Human, Elf, Wizard, Orc):\n")

    hp1 = health()
    sp1 = strength()
    print()
    print("Hero 1:", name1, " , ", type1)
    print("HEALTH of hero 1:", hp1)
    print("Strength of hero 1:", sp1)
    print()
    print("Who are they battling?")
    print()
    name2 = input("Name your Hero 2:\n")
    type2 = input("Character Type (Human, Elf, Wizard, Orc):\n")
    hp2 = health()
    sp2 = strength()
    print("Hero 2:", name2, " , ", type2)
    print("HEALTH of hero 2:", hp2)
    print("Strength of hero 2:", sp2)
    print()
    print("May your name go down in Legend....")
    print()

    time.sleep(5)
    os.system("clear")

    print("⚔️ BATTLE TIME ⚔️")
    print()
    round = 1
    winner = None

    while True:
        time.sleep(1)
        os.system("clear")
        print("⚔️ BATTLE TIME ⚔️")
        print()
        print("The battle continues!")
        print()

        c1Dice = rollDice(6)
        c2Dice = rollDice(6)

        difference = abs(sp1 - sp2) + 1

        if c1Dice > c2Dice:
            hp2 -= difference
            if round == 1:
                print(name1, "wins the first blow.")
            else:
                print(name1, "wins round", round)
        elif c2Dice > c1Dice:
            hp1 -= difference
            if round == 1:
                print(name2, "wins the first blow.")
            else:
                print(name2, "wins round", round)
        else:
            print("Their swords clash and they draw round", round)

        print()
        print(name1)
        print("HEALTH:", hp1)
        print()
        print(name2)
        print("HEALTH:", hp2)
        print()

        if hp1 <= 0:
            print(name1, "has died!")
            winner = name2
            break
        elif hp2 <= 0:
            print(name2, "has died!")
            winner = name1
            break
        else:
            print("And they're both standing for the next round")
            round += 1

    time.sleep(3)
    os.system("clear")
    print("⚔️ BATTLE TIME ⚔️")
    print()
    print(winner, "has won in", round, "rounds")
    break