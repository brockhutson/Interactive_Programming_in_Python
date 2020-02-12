# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:50:56 2019

@author: Brock

Week 3 Practice Problems
https://www.coursera.org/learn/interactive-python-1/supplement/HHeUN/practice-exercises-for-interactive-applications-optional
"""

## Printing "Goodbye" with a local message variable
#
####################################################
## Student should enter function on the next lines.
#def print_goodbye():
#    """Prints Goodbye to console."""
#    
#    message = "Goodbye"
#    print message
#
#
####################################################
## Tests
#
#message = "Hello"
#print message
#print_goodbye()
#print message
#
#message = "Ciao"
#print message
#print_goodbye()
#print message
#
#
####################################################
## Output
#
##Hello
##Goodbye
##Hello
##Ciao
##Goodbye
##Ciao

######################################################################
######################################################################
######################################################################
# Functions to manipulate global variable count

###################################################
# Student should enter function on the next lines.
# Reset global count to zero.
def reset():
    """Resets global count to 0"""
    global count
    count = 0
    
# Increment global count.
def increment():
    """Increments global count by 1"""
    global count 
    count += 1
    return count
    
# Decrement global count.
def decrement():
    """Decrements global count by 1"""
    global count
    count -= 1
    return count
    
# Print global count.
    """Prints global count"""
def print_count():
    print count

    
###################################################
# Test

# note that the GLOBAL count is defined inside a function
reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

####################################################
# Output
#1
#2
#-2


######################################################################
######################################################################
######################################################################

# Open a frame

###################################################
# Open frame
# Student should add code where relevant to the following.

import simplegui

message = "My first frame!"

# Handler for mouse click
def click():
    print message

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("My first frame", 100, 200)
frame.add_button("Click me", click)


frame.start()



######################################################################
######################################################################
######################################################################


# Open a frame

###################################################
# Open frame
# Student should add code where relevant to the following.

import simplegui 

message = "My second frame!"

# Handler for mouse click
def click():
    print message

# Assign callbacks to event handlers
frame = simplegui.create_frame("My second frame", 200, 100)
frame.add_button("Click me", click)


# Start the frame animation
frame.start()


######################################################################
######################################################################
######################################################################
 
##############
# Example of missing "global"

n1 = 0

def increment():
    n1 = n1 + 1

increment()
increment()
increment()

print n1


##############
# Example of missing "global"

n2 = 0

def assign(x):
    n2 = x

assign(2)
assign(15)
assign(7)

print n2


##############
# Example of missing "return"

n3 = 0

def decrement():
    global n3
    n3 = n3 - 1

x = decrement()

print "x = ", x
print "n = ", n


##############
# Example of print debugging

import simplegui

x = 0

def f(n):
    print "f: n,x = ", n, x
    result = n ** x
    print "f: result = ",result
    return result
    
def button_handler():
    global x
    print "bh : x = ", x
    x += 1
    print "bh : x = ", x

def input_handler(text):
    print "ih : text = ", text
    print f(float(text))
    
frame = simplegui.create_frame("Example", 200, 200)
frame.add_button("Increment", button_handler)
frame.add_input("Number:", input_handler, 100)

frame.start()



    

 # calculator with all buttons


import simplegui

# intialize globals
store = 0
operand = 0


# event handlers for calculator with a store and operand

def output():
    """prints contents of store and operand"""
    print "Store = ", store
    print "Operand = ", operand
    print ""
    
def swap():
    """ swap contents of store and operand"""
    global store, operand
    store, operand = operand, store
    output()
    
def add():
    """ add operand to store"""
    global store
    store = store + operand
    output()

def sub():
    """ subtract operand from store"""
    global store
    store = store - operand
    output()

def mult():
    """ multiply store by operand"""
    global store
    store = store * operand
    output()

def div():
    """ divide store by operand"""
    global store
    store = store / operand
    output()

def enter(t):
    """ enter a new operand"""
    global operand
    operand = int(t)
    output()
    
# create frame
f = simplegui.create_frame("Calculator",300,300)

# register event handlers and create control elements
f.add_button("Print", output, 100)
f.add_button("Swap", swap, 100)
f.add_button("Add", add, 100)
f.add_button("Sub", sub, 100)
f.add_button("Mult", mult, 100)
f.add_button("Div", div, 100)
f.add_input("Enter", enter, 100)


# get frame rolling
f.start()




######################################################################
######################################################################
######################################################################
 """
https://www.coursera.org/learn/interactive-python-1/supplement/ZNw6Z/practice-exercises-for-button-and-input-fields-optional
"""

   
import simplegui 


# Handlers for buttons
def print_hello():
    print 'Hello'
    
def print_goodbye():
    print 'Goodbye'

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Hello and Goodbye", 200, 200)
frame.add_button("Hello", print_hello)
frame.add_button("Goodbye", print_goodbye)


# Start the frame animation
frame.start()



# Register three buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 
color = None

# Handlers for buttons
def set_red():
    global color
    color = "red"
    frame.set_canvas_background('Red')
    
def set_blue():
    global color
    color = "blue"
    frame.set_canvas_background('Blue')
    
def print_color():
    print color

# Create frame
frame = simplegui.create_frame("Set and print colors", 200, 200)

frame.add_button('Red', set_red, 50)
frame.add_button('Blue', set_blue, 50)



# Start the frame animation
frame.start()



# GUI with buttons to manipulate global variable count

###################################################
# Student should enter their code below


import simplegui
count = None

# Define event handlers for four buttons
def reset():
    global count
    count = 0
#    print_count()
    
def increment():
    global count
    count += 1
#    print_count()
    
def decrement():
    global count
    count -= 1
#    print_count()
    
def print_count():
    global count
    print count
    
# Create frame and assign callbacks to event handlers


# Start the frame animation
    
    
# Echo an input field

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Handlers for input field
def get_input(text):
    print text
    
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Echo input", 200, 200)
inp = frame.add_input('Enter here', get_input, 50)

# Start the frame animation
frame.start()


# Convert input text into Pig Latin

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Pig Latin helper function
def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""
    
    first_letter = word[0]
    rest_of_word = word[1 : ]
    
    # Student should complete function on the next lines.
    
    if (first_letter == "a" or first_letter == "e" or first_letter == "i" or
        first_letter == "o" or first_letter == "u"):
        return word + 'way'
    else:
        return rest_of_word + first_letter + 'ay'
    
# Handler for input field
def get_input(word):
    print pig_latin(word)
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Pig Latin translator", 200, 200)
input = frame.add_input("Enter word here:", get_input, 50)

# Start the frame animation
frame.start()


http://www.codeskulptor.org/#user46_pHLYSSGvzk_0.py

######################################################################
######################################################################
######################################################################
    """
    CANVAS DRAWING
    """

# first example of drawing on the canvas

import simplegui

# define draw handler
def draw(canvas):
    canvas.draw_text("Hello!",[100, 100], 24, "White")
    canvas.draw_circle([100, 100], 2, 2, "Red")

# create frame
frame = simplegui.create_frame("Text drawing", 300, 200)

# register draw handler    
frame.set_draw_handler(draw)

# start frame
frame.start()


# example of drawing operations in simplegui
# standard HMTL color such as "Red" and "Green"
# note later drawing operations overwrite earlier drawing operations

import simplegui


# Handler to draw on canvas
def draw(canvas):
    canvas.draw_circle([100, 100], 50, 2, "Red", "Pink")
    canvas.draw_circle([300, 300], 50, 2, "Red", "Pink")
    canvas.draw_line([100, 100],[300, 300], 2, "Black")
    canvas.draw_circle([100, 300], 50, 2, "Green", "Lime")
    canvas.draw_circle([300, 100], 50, 2, "Green", "Lime")
    canvas.draw_line([100, 300],[300, 100], 2, "Black")
    canvas.draw_polygon([[150, 150], [250, 150], [250, 250], [150, 250]], 2, 
          "Blue", "Aqua")
    canvas.draw_text("An example of drawing", [60, 385], 24, "Black")

    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 400, 400)
frame.set_draw_handler(draw)
frame.set_canvas_background("Yellow")


# Start the frame animation
frame.start()

######################################################################
######################################################################
######################################################################
    
    """
    STRING PROCESSING
    """"
    
### String Processing

# String literals
s1 = "Rixner's funny"
s2 = 'Warren wears nice ties!'
s3 = " t-shirts!"
#print s1, s2
#print s3

# Combining strings
a = ' and '
s4 = "Warren" + a + "Rixner" + ' are nuts!'
print s4

# Characters and slices
print s1[3]
print len(s1)
print s1[0:6] + s2[6:]
print s2[:13] + s1[9:] + s3

# Converting strings
s5 = str(375)
print s5[1:]
i1 = int(s5[1:])
print i1 + 38





######################################################################
######################################################################
######################################################################
    """
    INTERACTIVE DRAWING
    """
    
# Handle single quantity
def convert_units(val, name):
    result = str(val) + " " + name
    if val > 1:
        result = result + "s"
    return result
        
# convert xx.yy to xx dollars and yy cents
def convert(val):
    # Split into dollars and cents
    dollars = int(val)
    cents = int(round(100 * (val - dollars)))

    # Convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")

    # return composite string
    if dollars == 0 and cents == 0:
        return "Broke!"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string
    
    
# Tests
print convert(11.23)
print convert(11.20) 
print convert(1.12)
print convert(12.01)
print convert(1.01)
print convert(0.01)
print convert(1.00)
print convert(0)


# interactive application to convert a float in dollars and cents

import simplegui

# define global value

value = 3.12

# Handle single quantity
def convert_units(val, name):
    result = str(val) + " " + name
    if val > 1:
        result = result + "s"
    return result
        
# convert xx.yy to xx dollars and yy cents
def convert(val):
    # Split into dollars and cents
    dollars = int(val)
    cents = int(round(100 * (val - dollars)))

    # Convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")

    # return composite string
    if dollars == 0 and cents == 0:
        return "Broke!"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string
    

# define draw handler
def draw(canvas):
    canvas.draw_text(convert(value), [60, 110], 24, "White")


# define an input field handler
def input_handler(text):
    global value
    value = float(text)


# create frame
frame = simplegui.create_frame("Converter", 400, 200)

# register event handlers
frame.set_draw_handler(draw)
frame.add_input("Enter value", input_handler, 100)


# start frame
frame.start()



######################################################################
######################################################################
######################################################################
    
# Print to canvas

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Draw handler
def draw(canvas):
    canvas.draw_text("It works!",[120, 112], 48, "Red")
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("It works", 400, 200)


frame.set_draw_handler(draw)

frame.start()



# Display "This is easy?"

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Draw handler
def draw(canvas):
    canvas.draw_text("This is easy", [200, 100], 24, 'blue')
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("This is easy", 400, 200)
frame.set_draw_handler(draw)


# Start the frame animation
frame.start()





# Display an X

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Draw handler
def draw(mark):
    mark.draw_text('X', [0,48], 48, 'white')
    mark.draw_text('X', [0,32], 48, 'red')


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("X marks the spot", 96, 96)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()


# Define a function that returns formatted minutes and seconds

###################################################
# Time formatting function
# Student should enter function on the next lines.
def format_time(seconds):
    secs = seconds % 60
    mins = seconds / 60
    
    return '%d minutes and %d seconds' % (mins, secs)


###################################################
# Tests

print format_time(23)
print format_time(1237)
print format_time(0)
print format_time(1860)

###################################################
# Output to console
#0 minutes and 23 seconds
#20 minutes and 37 seconds
#0 minutes and 0 seconds
#31 minutes and 0 seconds

######################################################################
######################################################################
######################################################################
    
# Move a ball

###################################################
# Student should add code where relevant to the following.


import simplegui 

# Define globals - Constants are capitalized in Python
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20

# Draw handler
def draw(canvas):
    canvas.draw_circle([WIDTH // 2, HEIGHT // 2], 
                       ball_radius, 2, 'Red', 'Red')
    
# Event handler for buttons
def increase_radius():
    global ball_radius
    ball_radius += RADIUS_INCREMENT

def decrease_radius():
    global ball_radius
    if ball_radius > RADIUS_INCREMENT:
        ball_radius -= RADIUS_INCREMENT


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("Increase radius", increase_radius)
frame.add_button("Decrease radius", decrease_radius)


# Start the frame animation
frame.start()





######################################################################
######################################################################
######################################################################
    




######################################################################
######################################################################
######################################################################
    




######################################################################
######################################################################
######################################################################
    




######################################################################
######################################################################
######################################################################
    




######################################################################
######################################################################
######################################################################
    