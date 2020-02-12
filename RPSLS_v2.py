# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:08:24 2019

@author: Brock
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:10:26 2019

@author: Brock

Rock-Paper-Scissors-Lizard-Spock v2
-added actions to results according to the game:
    
    Scissors cuts paper
    Paper covers rock
    Rock crushes lizard
    Lizard poisons Spock
    Spock smashes scissors
    Scissors decapittates lizard
    Lizard eats paper
    Paper disproves Spock
    Spock vaporizes rock

    and as it always has been
    
    Rock crushes scissors
"""
import random

def name_to_number(name):
    """
    Given string name, return integer 0, 1, 2, 3, or 4
    corresponding 'rock', 'Spock', 'paper', 'lizard', 'scissors'
    """

    if name == 'rock':
        number = 0
    elif name == 'Spock' or name == 'spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else:
        print("Please enter either 'rock', 'paper', 'scissors', 'lizard', 'Spock'")
    return number


def number_to_name(number):
    """
    Given integer number (0, 1, 2, 3, or 4)
    corresponding name from video
    """

    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        print("Please enter a number in the range of 0 - 4")
    return name


def rpsls_action(first, second):
    if first == 'scissors':
        if second == 'paper':
            action = 'cuts'
        elif second == 'lizard':
            action = 'decapitates'
        return action

    if first == 'paper':
        if second == 'rock':
            action = 'covers'
        elif second.lower() == 'spock':
            action = 'disproves'
        return action

    if first == 'rock':
        if second == 'lizard':
            action = 'crushes'
        elif second == 'scissors':
            action = 'crushes'
        return action

    if first == 'lizard':
        if second.lower() == 'spock':
            action = 'poisons'
        elif second == 'paper':
            action = 'eats'
        return action

    if first.lower() == 'spock':
        if second == 'scissors':
            action = 'smashes'
        elif second == 'rock':
            action = 'vaporizes'
        return action
    


def rpsls(player_choice):
    """
    Given string player_choice, play a game
    of RPSLS and print results to console
    """
    if player_choice == 'spock':
        player_choice = 'Spock'
    print("")
    print("Player has chosen", player_choice + '!')
    player_number = name_to_number(player_choice)

    comp_number = random.randrange(0,4)
    comp_choice = number_to_name(comp_number)
    print("The computer has chosen", comp_choice + '!')
    print('')

    result = (player_number - comp_number) % 5
    

    if result == 3 or result == 4:
        print('Computer wins!')
        action = rpsls_action(comp_choice, player_choice)
#        print(comp_choice, 'beats', player_choice)
        print(comp_choice, action, player_choice)

    elif result == 1 or result == 2:
        print('Player wins!')
        action = rpsls_action(player_choice, comp_choice)
#        print(player_choice, 'beats', comp_choice)
        print(player_choice, action, comp_choice)
    else:
        print('Tie, try again!')
