#!/usr/bin/env python

'''
Game of Sticks:
Human v. Human Sticks
Hat Tip: http://nifty.stanford.edu/2014/laaksonen-vihavainen-game-of-sticks/handout.html
'''

"Global Variables"
prompt = '>>> ' 
btw_1_3 = 'Please pick a number beteween 1 and 3.'
#player_1 = 0
#player_2 = 0

raw_input("Welcome to the game of sticks! Press <Enter> to continue...")




print("How many sticks are there on the table initially (10-100)?")
num_sticks = int(raw_input(prompt))
print("Ok, there are %s sticks on the board.") % (num_sticks)
print("|")*num_sticks

while num_sticks!=0:
	#player 1
	while True:
		print "Player 1: How many sticks do you take (1-3)?"
		player_1 =  int(raw_input(prompt))
		
		if 1 <= player_1 <= 3:
			break
		else:
			print (btw_1_3)

	num_sticks = num_sticks - player_1
	if num_sticks == 1:
		print("Ok, there is %s stick on the board.") % (num_sticks)
		print("|")*num_sticks

	elif num_sticks == 0:
		print("Player 1, you lose.")
		break
	else:
		print("Ok, there are %s sticks on the board.") % (num_sticks)
		print("|")*num_sticks


	#player 2
	while True:
		print "Player 2: How many sticks do you take (1-3)?"
		player_2 =  int(raw_input(prompt))
		
		if 1 <= player_2 <= 3:
			break
		else:
			print (btw_1_3)

	num_sticks = num_sticks - player_2
	if num_sticks == 1:
		print("Ok, there is %s stick on the board.") % (num_sticks)
		print("|")*num_sticks

	elif num_sticks == 0:
		print("Player 2, you lose.")
		break
	else:
		print("Ok, there are %s sticks on the board.") % (num_sticks)
		print("|")*num_sticks













'''
	#Player 1
	while player_1 < 1 or player_1 > 3:
		print "Player 1: How many sticks do you take (1-3)?"
		player_1 =  int(raw_input(prompt))

		if player_1 > 3 or player_1 < 1:
			print btw_1_3
			raw_input("Press <Enter> to continue...")

			print "Player 1: How many sticks do you take (1-3)?"
			player_1 =  int(raw_input(prompt))
		else:
			num_sticks = num_sticks - player_1

			if num_sticks == 1:
				print "There is %s stick on the board" % (num_sticks)

			elif num_sticks > 1:
				print "There are %s sticks on the board" % (num_sticks)

			elif num_sticks <= 0:
				print "Player 1, you lose."



	#player 2	
	print "Player 2: How many sticks do you take (1-3)"
	player_2 = int(raw_input(prompt))
	if player_2 > 3 or player_2 < 1:
		print btw_1_3
	else:
		num_sticks = num_sticks - player_2

		if num_sticks == 1:
			print "There is %s stick on the board" % (num_sticks)

		elif num_sticks > 1:
			print "There are %s sticks on the board" % (num_sticks)

		elif num_sticks <= 0:
			print "Player 2, you lose."
'''




