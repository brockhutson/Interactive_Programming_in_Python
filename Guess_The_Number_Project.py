# -*- coding: utf-8 -*-
"""

@author: Brock
Python 2.7

Codesculptor link: http://www.codeskulptor.org/#user46_7HJDx31gZu_0.py

This script is a guess the number game which illustrates an example for best case binary search.

"""

import simplegui
import math
import random

guess = 0
secret_number = None
count = 0
count_limit = 0


def new_game():
    global secret_number, count, count_limit, guess
    
    guess = 0
    secret_number = None
    count = 0
    count_limit = 0
    
    while secret_number != None:
        input_guess(guess)
    
    return count
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    
    secret_number = random.randint(0, 100)
    print "A number between 0 - 100 has been selected"
    print "How many guesses will it take you to guess the number?"
    print "Good luck"
    print ""
    print "Make your guess"
    
    return secret_number

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    
    secret_number = random.randint(0, 1000)
    print "A number between 0 - 1000 has been selected"
    print "How many guesses will it take you to guess the number?"
    print "Good luck"
    print ""
    print "Make your guess"
    
    return secret_number


def max_guess(maxg):
    global count_limit
    count_limit = int(maxg)
    if count_limit > 0:
        if count >= count_limit:
            print "Sorry, you are out of guesses, you lose!"
            print ""
            print "Try again!"
            return new_game()
            
        else:
            guesses_remaining = count_limit - count
            print "You have " + str(guesses_remaining) + " remaining"
    return count_limit

    
def input_guess(my_guess):
    # main game logic goes here	
    global count, secret_number, count_limit
    
    guess = int(my_guess)

    if guess < secret_number:
        print "Higher than " + str(guess)
        count += 1
        max_guess(count_limit)
        #print count_limit
    elif guess > secret_number:
        print "Lower than " + str(guess)
        count += 1
        max_guess(count_limit)
        #print count_limit
    elif guess == secret_number:
        if count == 1:
            print "Great job, only one guess!"
            print "The correct number was "  + str(guess) + "!"
        else:
            print "Correct, you win!"
       
   
    
# create frame
frame = simplegui.create_frame('Guess the Number', 300, 300)


# register event handlers for control elements and start frame
frame.add_button('Range is [0 - 100)', range100, 100)
frame.add_button('Range [0 - 1000)', range1000, 100)
frame.add_input('Enter guess', input_guess, 100)
frame.add_input('Enter guess max', max_guess, 100)

# call new_game 
new_game()