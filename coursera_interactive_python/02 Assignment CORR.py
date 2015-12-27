""" Guess the Number """

# http://codeskulptor.appspot.com/save/

# input will come from buttons and an input field

import simplegui
import random

high_limit = 100
guesses_remaining = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global guesses_remaining
    
    if high_limit == 100:
        guesses_remaining = 7
    else:
        guesses_remaining = 10
    secret_number = random.randrange(0, high_limit)
    print
    print 'New Game'
    print 'Range is 0 to', high_limit
    print 'Guesses Remaining', guesses_remaining
    print

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global high_limit
    hight_limit = 100
    new_game()
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global high_limit
    high_limit = 1000
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here	
    global guesses_remaining
    int_guess = int(guess)
    print 'Guess was', int_guess
    
    if int_guess == secret_number:
        print 'Correct'
        new_game()
        return
    elif int_guess > secret_number:
        print 'Lower'
    else:
        print 'Higher'
    
    
    guesses_remaining -= 1

    
    if guesses_remaining:
        print 'Guesses Remaining', guesses_remaining
    else:
        print 'No Guesses Remaining'
        new_game()
    print
    
# create frame
frame = simplegui.create_frame('Guess the Number', 200, 200)

# register event handlers for control elements and start frame
inp = frame.add_input('Guess', input_guess, 100)
button1 = frame.add_button('Range: 0 - 100', range100)
button2 = frame.add_button('Range: 0 - 1000', range1000)
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
