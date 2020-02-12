# -*- coding: utf-8 -*-
"""

@author: Brock
Python 2.7

Codeskulptor link: http://www.codeskulptor.org/#user46_NYT4rvVGXLMVzsc_0.py

This is a 1-player version of the stopwatch game.
"""


import simplegui

# define global variables
stopwatch = ''
total_ticks = 0
time = 0
timer_counter = 0
click = 0
score = 0

WIDTH = 180
HEIGHT = 140




# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    global stopwatch
    mins = time / 600
    secs = time % 600
    ones = secs % 100
    
    b = secs / 100
    c = ones / 10
    d = time % 10
    
    A = str(mins)
    B = str(b)
    C = str(c)
    D = str(d)

    stopwatch = A + ':' + B + C +'.' + D
    return stopwatch
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global time
    timer.start()
    
def stop():
    global time, stopwatch, score, total_ticks, click
    total_ticks += 1
    timer.stop()
    if stopwatch[-1] == '0':
        click += 1
        
def reset():
    global time, click, total_ticks
    time = 0
    click = 0
    total_ticks = 0
    
def scoreboard(score):
    global total_ticks
    score = str(click) + '/' + str(total_ticks)
    return score
    
def timer_handler():
    global time
    time += 1
    
# define event handler for timer with 0.1 sec interval
timer = simplegui.create_timer(100, timer_handler)

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [WIDTH // 3, HEIGHT // 1.75], 24, 'White')
    canvas.draw_text(scoreboard(time), [WIDTH // 1.25, HEIGHT // 5], 24, 'White')
    
# create frame
frame = simplegui.create_frame("Stopwatch Game", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)                               

# start frame

frame.start()

