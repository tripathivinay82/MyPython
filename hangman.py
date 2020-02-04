# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 20:56:47 2020

@author: vinayt
"""

import random 
# Function to display hangman
def display_hangman(attempt):
    
    if attempt == 0:        
        print(f"********************")
        print(f"     Hangman#       ")                
        print("_____________________")
        print("          |          ")
        print("        (^.^)        ")
        print("          |          ")
        print("         /|\         ")
        print("        / | \        ")
        print("       /  |  \       ")
        print("          |          ")
        print("         / \         ")
        print("        /   \        ")
        return 
    
    elif attempt == 1:   
        print(f"********************")
        print(f"     Hangman#       ")                
        print("_____________________")
        print("          |          ")
        print("        (^.^)        ")
        print("          |          ")
        print("         /|\         ")
        print("        / | \        ")
        print("       /  |  \       ")
        print("          |          ")
        print("         /           ")
        print("        /            ")
        return
    
    elif attempt == 2:
        print(f"********************")
        print(f"     Hangman#       ")                
        print("_____________________")
        print("          |          ")
        print("        (^.^)        ")
        print("          |          ")
        print("         /|\         ")
        print("        / | \        ")
        print("       /  |  \       ")
        print("          |          ")
        print("                    ")
        print("                    ")
        return
    
    elif attempt == 3:
        print(f"********************")
        print(f"     Hangman#       ")                
        print("_____________________")
        print("          |          ")
        print("        (^.^)        ")
        print("          |          ")
        print("         /|          ")
        print("        / |          ")
        print("       /  |          ")
        print("          |          ")
        print("                     ")
        print("                     ")
        return
    
    elif attempt == 4:
        print(f"********************")
        print(f"     Hangman#       ")                
        print("_____________________")
        print("          |          ")
        print("        (^.^)        ")
        print("          |          ")
        print("          |          ")
        print("          |          ")
        print("          |          ")
        print("          |          ")
        print("                     ")
        print("                     ")
        return
    
    elif attempt == 5:
        print(f"********************")
        print(f"     Hangman#       ")                
        print("_____________________")
        print("          |          ")
        print("        (^.^)        ")
        print("                     ")
        print("                     ")
        print("                     ")
        print("                     ")
        print("                     ")
        print("                     ")
        print("                     ")
        return
    
    elif attempt == 6:
        print(f"********************")
        print(f"     Hangman#       ")                
        print("*********************")        
        print("*****GAME OVER*******") 
        print("*********************")        
        print("_____________________")
        print("          |          ")
        print("                     ")
        print("                     ")
        print("                     ")
        print("                     ")
        print("                     ")
        print("                     ")
        print("                     ")
        print("                     ")
        return
    
# Function to get the word as per game level entered by player
def choose_game_word(wlen):
    
    #Read the word file 
    with open('sowpods.txt') as file_object:
        contents = file_object.read()
        #Split the words and save in list
        word=contents.split()
        
    new_word=[]
    for x in word:
        if len(x) < wlen:
            new_word.append(x)
        elif wlen == 3:
            return random.choice(word)            
            pass
    return random.choice(new_word)

# Play the game    
def play_hangman():

    #Get player input for game difficulty level
    uinput = int(input("Choose the Level of Hangman Game \n  1) Less than 5 words; \n 2) less than 8 words; \n 3) Any word: "))
    dlevel=uinput
    if uinput == 1:
       uinput=4
       game_word=choose_game_word(uinput)
       if not game_word:
           print(f"There is no word matching user input; input:{uinput}; word: {game_word}")
           return
    elif uinput == 2:
       uinput=7
       game_word=choose_game_word(uinput)
       if not game_word:
           print(f"There is no word matching user input; input:{uinput}; word: {game_word}")
           return
    elif uinput == 3:
       game_word=choose_game_word(uinput)    
    
    #print(f" Game Word: {game_word}")

    #Start The Game
    print(f"*********************************************")
    print(f"**********USER INPUT*************************")
    print(f"**********Difficulty Level: {dlevel}*********")
    print(f"*********************************************")

    #Show the word in dash format for the game
    glen=[]
    for x in range(len(game_word)):
        glen.append('_')
    
    c1=0
    print(display_hangman(c1))
    gword=set()
    
    #Copy selected game workd in another variable and make new var a list
    temp_game_word=game_word
    temp_game_word=list(temp_game_word)
    
    c2=1

    while True:
                
        print(f"List of Incorrect Letter Guessed by User: {gword}")
        print(f"Challenge Word: {glen}")    
        uWord=str(input("Enter You Guess: "))
        uWord=uWord.upper()
        
        if game_word.find(uWord) == -1:
            gword.add(uWord)
            print(f"Oops! You guessed the wrong letter: {uWord}")
            c1=c1+1
            display_hangman(c1)
        else:
            #print(f"game_word = {game_word}")
            wloc=game_word.index(uWord)
            #This is needed if string has duplicate letters
            temp_wloc=temp_game_word.index(uWord)
            temp_game_word.insert(1,temp_wloc)
            glen[wloc]=uWord
            print(f"Congratulations!! for the correct guess: {uWord}")
            display_hangman(c1)
            print(f"Updated Challenge Word: {glen}")
        
        ugWord=''.join(glen)
        if game_word == ugWord:
            print(f"******************************************************************************")
            print(f"Congratulation! You have successfully guessed all the letters; its {ugWord}")
            print(f"Challenge Word: {game_word}")
            print(f"List of Incorrect Letter Guessed by User: {gword}")
            print(f"******************************************************************************")
            return
        if c1 == 6:
            print(f"*********************************************")
            print("Sorry you have used all the lifeline... Game Over...")
            print(f"Challenge Word: {game_word}")
            print(f"List of Incorrect Letter Guessed by User: {gword}")
            print(f"*********************************************")
            return

#Play the game    
play_hangman()









        