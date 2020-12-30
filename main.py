from numpy import random

num = random.randint(10)
print("Guess number from 1 - 10")
userInput = int(input())

while userInput!= num:
    # if user guess is wrong
    if userInput > num:
        userInput = int(input("Wrong guess, your guess is more than actual answer. Try again "))
    if userInput < num:
        userInput = int(input("Wrong guess, your guess is less than actual answer. Try again "))

   # if user guess the right number
    if userInput == num:
        print("Congratulations!! you guessed the right number")
        print("Game Over, You WIN!!!")
