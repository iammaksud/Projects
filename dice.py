import random

while True:
    ask = input("Roll the dice(y,n): ")

    if ask == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'({die1},{die2})')
    elif ask == 'n':
        print("BYE BYE LOSERRRR")
        break
    else:
        print("GO AWAY")    