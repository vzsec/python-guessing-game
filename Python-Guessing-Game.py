import random
import time

num = random.randrange(1, 1000) # Computer Selects Its Number

print("Welcome to my game.....") # Intro to game
time.sleep(2)
intro = ["Guess!", "That!", "Number!"] 
i = 0
while i <= 2:
    print(intro[i])
    time.sleep(1)
    i = i + 1
time.sleep(2)
print("\n" * 50)

while True: # Ensure first guess is a real number
    try:
        guess = int(input("Please enter your first guess: "))
        break
    except:
        print("Please enter a valid number")


count = 1 # Defining number of guesses variable

if guess > num: # Check first guess compared to computers number
    print("Your first guess is too high! Try again!")
elif guess < num:
    print("Your first guess is too low! Try again!")

while guess != num: # Loop if proceeding guesses are high or low and if they enter in legit numbers
    try:
        guess = int(input("Your new guess: "))
        count = count + 1
    except:
        print("Please enter a valid number")
        continue
    if guess > num:
        print("Your guess is too high! Try again!")
    elif guess < num:
        print("Your guess is less than my number! Try again!")

print("You found my number! Great job!") # Finding the winning number
print("It took you " + str(count) + " guesses to figure out the number!") # Final score on how many guesses it took
