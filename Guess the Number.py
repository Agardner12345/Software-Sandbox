import random

x = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100.")

attempts = 5

def remaining_attempts():
    global attempts
    attempts -= 1
    print(f"You have {attempts} attempts remaining.")

user_input = False
while user_input == False:
    try:
        answer = input("Can you guess the number?")
        answer = int(answer)
    except ValueError:
        print("Sorry, that isn't a number.")
        continue
    if answer == x:
        user_input = True
        print("That's correct! Congratulations!")
    elif attempts == 1:
        user_input = True
        print(f"You are out of attempts. The number was {x}. You lose.")
    elif answer > x and answer <= 100:
        print("Too high!")
        remaining_attempts()
    elif answer > 100:
        print("WAY too high!")
        remaining_attempts()
    elif answer < x and answer >=1:
        print("Too low!")
        remaining_attempts()
    elif answer < 1:
        print("WAY too low!")
        remaining_attempts()


    
