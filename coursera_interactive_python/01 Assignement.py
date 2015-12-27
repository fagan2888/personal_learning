# http://codeskulptor.appspot.com/save/
# interactivepython@online.rice.edu	

""" Assignement of Week 1 - Rock, Scissor, Paper, Lizard, Spock """

import math 
import random

""" Helper Functions: The idea of this program is to equate the strings "rock", 
"paper", "scissors", "lizard", "Spock" to numbers as seen below and then back:

 0 - rock
 1 - Spock
 2 - paper
 3 - lizard
 4 - scissors

"""

# Helper Function nb.1 - converts the string name into a number between 0 and 4
def name_to_number(name) :
    if name == "rock" :
    	return 0 
	elif name == "Spock" :
		return 1 
	elif name == "paper" :
		return 2
	elif name == "lizard" :
		return 3
	elif name == "scissors" :
		return 4
	else :
		print "N/A"
    

# Helper Function nb.2 - converts the numbers between 0 and 4 to the string name
def number_to_name(number) :
	if number == 0 :
    	return "rock"
	elif number == 1 :
		return "Spock" 
	elif number == 2 :
		return "paper"
	elif number == 3 :
		return "lizard"
	elif number == 4 :
		return "scissors"
	else :
		print "N/A"
    


# Implement the first part of the main function.
def rpsls(player_choice) :
	player_number = random.randrange(0, 5)
	player_choice = number_to_name(player_number)
    return player_number


# print a blank line to separate consecutive games
print ""
# print out the message for player's choice
print "The player chooses ", number_to_name(player_choice)
# print out the message for computer's choice
print "The computer chooses ", number_to_name(comp_choice)

# if (comp_number - player_number) % 5 == 1 or winner ==2

# compute difference of comp_number and player_number modulo five
# use if/elif/else to determine winner, print winner message
def conditonal(player_choice - comp_choice) :
	x = rpsls(random.randrange(0, 5), random.randrange(0, 5))
		if x < 1 :
			print "Computer wins!"
		elif > 0 :
			print "Player wins!" 
		elif x :
			print "Player/Computer wins!"
		elif x :
			print "Player and computer tie!"
		else :
			print "N/A"
	return x

# convert name to player_number using name_to_number  
def rpsls(name):
    player_number = name_to_number(name)    
     
# compute random guess for comp_number using random.randrange()  
	comp_number = random.randrange(0, 5)

# compute difference of player_number and comp_number modulo five    
    difference = (player_number - comp_number) % 5
        if difference == 2:
            print "Computer wins!"
        elif difference == 1:
            print "Computer wins!"
        elif difference == 0:
            print "Computer and player tie!"
        elif difference == 3:
            print "Player wins!"
        elif difference == 4:
            print "Player wins!"
        else :
            print "na"


#GAMES TO BE PLAYED

def rpsls(name):
    player_number=name_to_number(name)
   
    comp_number=random.randrange(0,4)
    print ""
    if (player_number-comp_number)%5==1 or (player_number-comp_number)%5==2:
        print "Player chooses", name
        print "Computer chooses", number_to_name(comp_number)
        print "Player Wins"
    elif (player_number-comp_number)%5==3 or (player_number-comp_number)%5==4:
        print "Player chooses", name
        print "Computer chooses", number_to_name(comp_number)
        print "Computer wins"
    elif (player_number-comp_number)%5==0:
        print "Player chooses", name
        print "Computer chooses", number_to_name(comp_number)
        print "Ties"
    else: print "something wrong"

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")


""" 
peer 1 → Unfortunately, there are several errors in your program that stop 
it from running completely. I gave credit based on what I could figure out from 
the code. The program basically needs to be rewritten. I suggest you send the 
link to your project to interactivepython@online.rice.edu <---- this is the 
Code Clinic
peer 4 → Even after I indented it, it threw an error as player_name 
was not defined. 1.Indentation error. 2.Player_name not defined. 3.The function 
difference takes no arguements but two arguements are passed. Just keep in mind 
that in python we don't use braces so indentation is very important.
"""

