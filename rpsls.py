# The program simulates playing Rock-paper-scissors-lizard-Spock

import random

# This function is a helper function,
# which converts a name to the corresponding number
def name_to_number(name):
	if name == 'rock':
		return 0
	elif name == 'Spock':
		return 1
	elif name == 'paper':
		return 2
	elif name == 'lizard':
		return 3
	elif name == 'scissors':
		return 4
	else:
		return 5

# This function is a helper function,
# which converts a number to the corresponding name
def number_to_name(number):
	if number == 0:
		return 'rock'
	elif number == 1:
		return 'Spock'
	elif number == 2:
		return 'paper'
	elif number == 3:
		return 'lizard'
	elif number == 4:
		return 'scissors'
	else:
		return 'wrong'

# This is the main function,
# which implements the main function of the program
def rpsls():
	player_number = random.randrange(0, 5)
	player_choice = number_to_name(player_number)
	print 'Player chooses ' + player_choice
	comp_number = random.randrange(0, 5)
	comp_choice = number_to_name(comp_number)
	print 'Computer chooses ' + comp_choice
	result = (player_number - comp_number) % 5
	if result == 0:
		print 'Player and computer tie!\n'
	elif result <= 2:
		print 'Player wins!\n'
	elif result <= 4:
		print 'Computer wins!\n'
	else:
		print 'Something wrong!\n'

# The calls of the rpsls function
rpsls()
rpsls()
rpsls()
rpsls()
rpsls()
