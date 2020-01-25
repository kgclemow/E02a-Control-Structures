#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!') # output greetings to the user
colors = ['red','orange','yellow','green','blue','violet','purple'] # defining the variable colors as the following colors
play_again = '' # defind play_again as the variable ' '
best_count = sys.maxsize            # the biggest number

while (play_again != 'n' and play_again != 'no'): # as long as play_again does not equal 'n' or 'no' continue the loop 
    match_color = random.choice(colors) # match_color is equal to a random color of those listed above
    count = 0 # count is equal to 0 
    color = '' # color is equal to ' '
    while (color != match_color): # as long as color does not equal the random chosen color, continue this loop
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line # ask the user for an answer to the question
        color = color.lower().strip() # the answer can be any capitalization and spacing before or after 
        count += 1 # add 1 to the variable count 
        if (color == match_color): # if the user color is equivalent to the random color 
            print('Correct!') # tell them correct 
        else: # defining a condition 
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) # other than correct answer, tell them wrong and how many guesses they have had 
    
    print('\nYou guessed it in {} tries!'.format(count)) # when correct answer, tell them how many tried it took 

    if (count < best_count): # condition of if count is smaller than the biggest number
        print('This was your best guess so far!') # tell user the following 
        best_count = count # biggest number is equal to 0 plus 1 

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip() # ask if they want to play again with answer being any capitalization or spacing before or after 

print('Thanks for playing!') # tell user thanks 