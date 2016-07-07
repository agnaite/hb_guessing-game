# Put your code here

import random         #importing the random library to use the random number generator

def num_guess_game():                                                   #creates a random number guessing game function
    name = raw_input("Hi! What's your name? ")                          #asks the user for their name and stores it in a variable
    print "Hi, %s" % name                                               #greets the user with their name
    guess = raw_input("Please guess a number between 1 and 100! ")      #asks the user for their number guess and stores it in a variable
    count = 1                                                           #once the user guesses, the counter starts with their first guess

    correct_guess = random.randint(1, 100)                              #python generates a random number between 1 and 100 (inclusively) and stores the number in the variable

    while correct_guess != int(guess):                                  #creates a while loop - while the user's integer guess is not equal to Python's generated number do the following:
        try:
            guess = int(guess)                                          #it attempts to convert the user's guess to an integer, 
        except:
            print("Error. The value you entered is not a number. Bye!") #and if Python cannot, it displays an error message
        if guess > 100 or guess < 0:                                    #if the user's guess is greater than 100 or less than zero
            guess = raw_input("The number you have guessed is not between 1 and 100. Please try again.")    #inform the user and have them guess another number
            count += 1                                                  #even if the user's guess is not between 1 and 100, their guess is still counted
        elif guess > correct_guess:                                     # if the user's guess is greater than Python's generated number
            guess = raw_input("This is too high. Please guess again. ") # informs the user their guess is too high and stores their guess in the variable
            count += 1                                                  #even if the user's guess is too high, their guess is counted
        else:
            guess = raw_input("This is too low. Please guess again. ")  #otherwise, if the user's guess is too low, the program alerts the user and invites them to guess again and stores their guess in the variable
            count += 1                                                  #even if the user's guess is too low, their guess is counted

    print "You guessed the correct number! It took you %d tries to guess the correct number!" % count  #alerts the user that they've guessed the correct number and tells them how many times it took for them to correctly guess
    return count                                                        #the function returns the total number of times the user guessed and ends the function

choice = raw_input("Enter 'Y' to play or 'Q' to quit. ")                #the user is given the choice of playing the game again or quitting; their choice is stored in the variable
scores = []                                                             #creates an empty array

while choice.lower() != 'q':                                            #as long as the user chooses to play the game again
    scores.append(num_guess_game())                                     #calls the random number guessing game function to play again and adds the user's final score from each game to the scores array
    choice = raw_input("Enter 'Y' to play or 'Q' to quit. ")            #gives the user the choice to play the agame again and stores their choice in the variable

print "Your best score was %d!" % min(scores)                           #once the user chooses to quit, the program prints their best (lowest) score of all the games they've played.




