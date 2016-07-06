# Put your code here

import random

name = raw_input("Hi! What's your name? ")
print "Hi, %s" % name
guess = raw_input("Please guess a number between 1 and 100! ")

correct_guess = random.randint(1, 100)

while correct_guess != int(guess):
    if int(guess) > correct_guess:
        guess = raw_input("This is too high. Please guess again. ")
    else:
        guess = raw_input("This is too low. Please guess again.")

print "You guessed the correct number!"

