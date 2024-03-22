"""Number Guessing Game"""
from random import randint

SECRET: int = randint (1,5)
correct: bool = False

while not correct:
    guess: int= int(input("Guess a number"))
    if guess == SECRET: 
        print(f"Correct! {guess} is the number!")
    else:
        print("Not Correct!"+ "Guess Again!")

if guess < 1: 
    print(f"{guess} too low!")
if guess > 5:
    print (f"{guess} too high!")
