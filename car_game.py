command = " "
started = False
while True:
    command = input(">  ").lower()
    if command == "start":
        if started :
            print ("Hey, Car has already started!!")
        else:
            started = True
            print("Car started ... Ready to go ")

    elif command == "stop":
        if not started :
            print ("Hey, Car has already stopped!!")
        else :
            started = False
            print("Car stopped ...")

    elif command == "help":
        print ("""
Start - To stART THE car
Stop - To STOP THE car
Quit - To exit the game""")
    elif command == "quit" :
        break
    else :
        print ("Sorry, I don't understand that!")




