print("Welcome to the dungeon! You must escape.")

choice1 = input("You are at a crossroads. Turn left or right? left / right")
choice1 = choice1.lower()
if choice1== ('left'):
    choice2 = input("Would you like to swim across the moat or climb the ladder? swim / climb")
    choice2 = choice2.lower()
    if choice2 == ('climb'):
        choice3 = input("There are three doors. Choose one. red / blue / yellow")
        choice3 = choice3.lower()
        if choice3 == ('blue'):
            print("Congratulations! You have escaped!")
        else:
            print("You died :(")
    else:
        print("You died :(")
else:
    print("You died :(")
    
