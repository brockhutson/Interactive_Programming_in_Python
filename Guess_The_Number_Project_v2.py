# -*- coding: utf-8 -*-
"""

@author: Brock
Python 2.7

Codeskulptor Link: http://www.codeskulptor.org/#user46_6QE3Pkt5aY_0.py

This script is a guess the number game which illustrates an example for best case binary search.

"""

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

num_range = None

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_range
    if num_range == 100:
        range100()
    elif num_range == 1000:
        range1000()


# define event handlers for control panel
def range100():
    """
       Creates button that changes the range to [0,100) 
       and starts a new game
    """
    global num, chances, num_range
    
    
    num_range = 100
    num = random.randrange(0,100)
    chances = 7
    print "\nNew game"
    print "Range is 0 to 100"
    print "You have 7 guesses"


def range1000():
    """
       Creates button that changes the range to [0,1000) 
       and starts a new game
    """    
    global num, chances, num_range
    
    
    num_range = 1000
    num = random.randrange(0,100)
    chances = 10
    print "\nNew game"
    print "Range is 0 to 1000"
    print "You have 10 guesses"
        
def input_guess(guess):
    # main game logic goes here	
    
    global chances, num_range, num

    guess = int(guess)
    print "\nNumber of chances left ",chances
    print "Your guess is ", guess
    
    if num > guess:
        print 'Higher!'
    elif num < guess:
        print 'Lower!'
    elif num == guess:
        print 'Correct!!!'
        print "You Win!"
        print "Let's play another game."
        new_game()
    
    if chances == 0:
        print "Out of turns, You lose!"
        print "The number was", num
        print "Try again!"
        new_game()
        
# Create Frame
frame = simplegui.create_frame("Guess the Number", 300, 300)

#Control Elements
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_label("")
frame.add_input("Enter guess", input_guess, 200)
frame.add_label("")
frame.add_label("\nCan you guess the number?\nChoose between either 0 - 100 or 0 - 1000.") 

# Call new_game and Start frame
new_game()
frame.start()