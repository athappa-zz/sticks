#!/usr/bin/env python

'''
Game of Sticks:
Human v. Human Sticks
Hat Tip: http://nifty.stanford.edu/2014/laaksonen-vihavainen-game-of-sticks/handout.html
'''

import random

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


stick_dict={}
for number in range(1,num_sticks+1):
	stick_dict["hat{0}".format(number)]=[[1,2,3]]




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



	#test = [[1, 2, 3]]
	#guess = random.choice(test[0])


	#AI player
	guess = random.choice(stick_dict["hat{0}".format(num_sticks)][0])
	print guess


	#test.append(guess)

	stick_dict["hat{0}".format(num_sticks)].append(guess)
	print stick_dict

	#If the AI loses
	for key in stick_dict:
		if len(stick_dict[key]) == 2:
			del stick_dict[key][1]

	#If the AI wins
	for key in stick_dict:
	if len(stick_dict[key]) == 2:
		stick_dict[key][0].append(stick_dict[key][1])
		del stick_dict[key][1]

	break











'''
for element in stick_dict["hat{0}".format(num_sticks)][0]:
	print element
	#for number in element:
	if number == guess:
			element.remove(guess)
'''







