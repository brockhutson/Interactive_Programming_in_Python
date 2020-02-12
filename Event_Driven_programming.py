'''
    These scripts are all written using Codeskulptor which can be found at:
        
        http://www.codeskulptor.org/
    
    These scipts are also in Python 2.7
'''

# CodeSkulptor GUI module
#import simplegui
#
## Event handler
#def tick():
#    print "tick!"
#
## Register handler
#timer = simplegui.create_timer(1000, tick)
#
## Start timer
#timer.start()


#import simplegui
#
#message = "Welcome!"
#
## Handler for mouse click
#def click():
#    global message
#    message = "Good job!"
#
## Handler to draw on canvas
#def draw(canvas):
#    canvas.draw_text(message, [50,112], 36, "Green")
#
## Create a frame and assign callbacks to event handlers
#frame = simplegui.create_frame("Home", 300, 200)
#frame.add_button("Click me", click)
#frame.set_draw_handler(draw)
#
## Start the frame animation
#frame.start()

"""
Program Structures
    -Globals (state)
    -Helper functions
    -Classes(later)
    -Define event handlers
    -Create a frame
    -Register event handlers
    -Start frame and timers
"""

## Import the module
#import simplegui
#
## Define global variables (program state)
#counter = 0
## Define "helper" functions
#def increment():
#    global counter
#    counter += 1
#    
## Define event handler functions
#def tick():
#    increment()
#    print(counter)
#
#def buttonpress():
#    global counter
#    counter = 0
#    
## Create a frame
#frame = simplegui.create_frame("SimpleGUI Test", 100, 100)
#
## Register event handlers
#timer = simplegui.create_timer(1000, tick)
#frame.add_button("Click me!", buttonpress)
#
## Start frame and timers
#frame.start()
#timer.start()



##############
# Examples of simplifying conditionals

def f1(a, b):
    """Returns True exactly when a is False and b is True."""  
    if a == False and b == True:
        return True
    else:
        return False

def f2(a, b):
    """Returns True exactly when a is False and b is True."""  
    if not a and b:
        return True
    else:
        return False    

def f3(a, b):
    """Returns True exactly when a is False and b is True."""  
    return not a and b

def g1(a, b):
    """Returns False eactly when a and b are both True."""  
    if a == True and b == True:
        return False
    else:
        return True
    
def g2(a, b):
    """Returns False eactly when a and b are both True."""  
    if a and b:
        return False
    else:
        return True

def g3(a, b):
    """Returns False eactly when a and b are both True."""  
    return not (a and b)


######################################################################
######################################################################
######################################################################

