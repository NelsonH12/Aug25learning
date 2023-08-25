#Making a guess the number game off the top of my head.
#first time making something without a video tutorial to help.
#Task one will be to generate the random number
#Will need user input sections and a score variable.  Score tracks number of guesses

import random

correct_number = random.randint(1, 20)

score = 0

while True:
  guess = int(input("Guess a number between 1 and 20: "))

  if guess < correct_number:
    print("Too low, guess again")
    score = score + 1
    print("You've made " + str(score) + " guesses.")
  elif guess > correct_number:
    print("Too high, guess again")
    score = score + 1
    print("You've made " + str(score) + " guesses.")
  else: 
    score = score + 1
    print("Good job!  You guessed the correct number in " + str(score) + " guesses.")
    break