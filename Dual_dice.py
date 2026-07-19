import random

playing = True
while playing:
    choice = input("Roll the dice (y/n) : ".lower())
    if choice == "y":
        die_one = random.randint(1,6)
        die_two = random.randint(1,6)
        print (f"({die_one},{die_two})")
    elif choice == "n":
         playing = False
         print("Thanks for playing!")
         break
    else:
        print("Please enter a valid choice")

