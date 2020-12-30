# computer will pick the number
#  show rules, 
#  user write number, 
#  check if its the same number, 
#  else give hint

from numpy import random

num = random.randint(10)
print("Guess number from 1 - 10")
userInput = int(input())


while userInput!= num:
    userInput = int(input("Wrong guess, try again? "))

    if userInput == num:
        print("Congratulations!! you guessed the right number")
