# -*- coding: utf-8 -*-
"""
@author: Brock
python 2.7

Codeskulptor Link: http://www.codeskulptor.org/#user46_pl7hn57mYZ_1.py

This is a version of the game pong written using Codeskulptor.
"""

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True


# initialize ball_pos and ball_vel for new bal in middle of table

ball_vel = [0, 0]

# if direction is RIGHT, the ball's velocity is upper right, else upper left
direction = random.choice([LEFT, RIGHT])

def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos = [WIDTH // 2, HEIGHT // 2]
    direction = random.choice([LEFT, RIGHT])
    
    ball_vel[0] = random.randrange(2, 4)
    ball_vel[1] = random.randrange(2, 4)
  
    if direction is LEFT:
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = -ball_vel[1]
    elif direction is RIGHT:
        ball_vel[0] = ball_vel[0]
        ball_vel[1] = -ball_vel[1]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    score1 = 0
    score2 = 0
    
    paddle1_pos = HEIGHT // 2
    paddle2_pos = HEIGHT // 2
    
    paddle1_vel = 0
    paddle2_vel = 0
    
    direction = random.choice([LEFT, RIGHT])

    spawn_ball(direction)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
       ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] <= BALL_RADIUS:
       ball_vel[1] = -ball_vel[1]   
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, 'White', 'White')
        
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    if paddle1_pos - HALF_PAD_HEIGHT <= 0:
        paddle1_pos = HALF_PAD_HEIGHT 
    elif paddle1_pos + HALF_PAD_HEIGHT >= HEIGHT:
            paddle1_pos = HEIGHT - HALF_PAD_HEIGHT

    if paddle2_pos - HALF_PAD_HEIGHT <= 0:
        paddle2_pos = HALF_PAD_HEIGHT 
    elif paddle2_pos + HALF_PAD_HEIGHT >= HEIGHT:
            paddle2_pos = HEIGHT - HALF_PAD_HEIGHT

    
    # draw paddles
    canvas.draw_polygon([(0, paddle1_pos - HALF_PAD_HEIGHT),
                                   (PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT),
                                   (PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT),
                                   (0, paddle1_pos + HALF_PAD_HEIGHT)],
                                    1, 'White', 'White')
    
    canvas.draw_polygon([(WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT),
                                   (WIDTH, paddle2_pos - HALF_PAD_HEIGHT),
                                   (WIDTH, paddle2_pos + HALF_PAD_HEIGHT),
                                   (WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT)],
                                   1, 'White', 'White')
    
    # determine whether paddle and ball collide
    
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:
        if paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1] and paddle1_pos + HALF_PAD_HEIGHT >= ball_pos[1]:
            reflect()
        else:
            score2 += 1
            spawn_ball(direction)
            
    if ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
        if paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1] and paddle2_pos + HALF_PAD_HEIGHT >= ball_pos[1]:
            reflect()
            
        else:
            score1 += 1
            spawn_ball(direction)
        
    # draw scores
    canvas.draw_text(str(score1), [WIDTH * 0.25, HEIGHT * 0.5], 42, 'Green')
    canvas.draw_text(str(score2), [WIDTH * 0.75, HEIGHT * 0.5], 42, 'Red')

def reflect():
    global ball_vel
    ball_vel[0] = - ball_vel[0]
    ball_vel[0] *= 1.1
    ball_vel[1] *= 1.1    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 4
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel = -4
        
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 4
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -4 
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0

def reset():
    new_game()
    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.add_button("Reset", reset, 100)

# start frame
new_game()
frame.start()
    