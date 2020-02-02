# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 11:19:59 2020

@author: vinayt
"""
import sys

user1=input("Name of Player1:")
user2=input("Name of Player2:")

count=int(input("how many times do you want to play the game?"))
i=1

while i <= count:
    
    print("Game Number#" + str(i))
          
    user1_input=input("%s, do you want to rock/paper/scissors?" %user1)
    user2_input=input("%s, do you want to rock/paper/scissors?" %user2)

    def play_game (u1,u2):
    
        if u1 == u2:
            return("Guys..its a Tie!!")
        elif u1 == 'rock':
            if u2 == 'scissors':
                return("rock Wins!!")
            elif u2 == 'paper':
                return("paper wins!!")
        elif u1 == 'paper':
            if u2 == 'scissors':
                return("scissors wins!!")
            elif u2 == 'rock':
                return("papers wins")
        elif u1 == 'scissors':
            if u2 == 'paper':
                return("scissors wins")
            elif u2 == 'rock':
                return("rock wins!")
        else:
            return("Invalid Input...try again")
            sys.exit()
    
    print(play_game(user1_input,user2_input))
    i=i+1
    
            