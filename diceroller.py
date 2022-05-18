import random

print("welcome to the Dice Roller!")

while True:
    dice = input("Roll a dice in NdN format: ")

    try:
        rolls, limit = map(int, dice.split('d'))

    except Exception:
        print("Format has to be NdN!")


    result = ", ".join(str(random.randint(1, limit)) for r in range(rolls))
    print(result)

    again = input("Would you like to play again? Type 'y' for yes or 'n' for no: ").lower()

    if again == 'y':
        continue

    elif again == 'n':
        break
        
