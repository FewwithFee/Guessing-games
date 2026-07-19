import random

def roll_dice():
    return random.randint(1,6)

while True:
    input("Press Enter to roll the dice ")
    print (f"You rolled a {roll_dice()}")
    play_again = input("Would you like to play again? (y/n) : ").lower()
    if play_again != "y":
        print ("Thank you for playing")
        break
