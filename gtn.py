# Guess the number

import simplegui
import random
import math

# Global variables
secret = random.randrange(0, 100)
guess = 0
low = 0
high = 100
count = 7

# Helper functions
def new_game():
    """ set the secret number"""
    global secret, count
    secret = random.randrange(low, high)
    count = int(math.ceil(math.log(high - low + 1, 2)))
    print "Game restart"

# Event handlers
def basic_range():
    """ set the random range to [0, 100)"""
    global high
    high = 100
    new_game()
    print "New game with range [0, 100)"

def bigger_range():
    """ set the random range to [0, 1000)"""
    global high
    high = 1000
    new_game()
    print "New game with range [0, 1000)"

def input_guess(inp):
    """ get the number player inputs"""
    global guess, count
    guess = int(inp)
    print "Your guess is", guess
    count -= 1
    print "The remaining guesses are", count
    if secret == guess:
        print "Correct"
        new_game()
    elif count == 0:
        print "Fail"
        new_game()
    elif secret < guess:
        print "Lower"
    elif secret > guess:
        print "Higher"
    else:
        print "Error"

# Create the frame and register the handlers
frame = simplegui.create_frame("Guess the number", 300, 300)
frame.add_input("Your guess is:", input_guess, 100)
frame.add_button("New game", new_game, 100)
frame.add_button("Range: 0-100", basic_range, 100)
frame.add_button("Range: 0-1000", bigger_range, 100)

# Start the frame
frame.start()