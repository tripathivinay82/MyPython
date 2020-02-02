# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:51:19 2020

@author: vinayt
"""
import numpy as np

def play_game():
    global row 
    global column 
    
    rVal = input("Number of Rows and Colums for Board Game? e.g. [3x3]: ")
    rVal=rVal.split("x")
    row=int(rVal[0])
    column=int(rVal[1])
    count=row*column
    flag=1
    
    if row == column:
        pass
    else:
        print(f"Board Size is not correct!!! User Input:- Row: {row} and Column: {column}...it must be same")
        flag=0
        return flag
    
    #Initialize the board with all zero
    init_arr = np.zeros((row,column),dtype=np.int16)
    print(init_arr)

    nz = int(np.count_nonzero(init_arr))
    #print (f"Non Zero Elements in Array: {nz}")
    
    while count > nz:    
    
        #Start The Game
        p1_loc=input("Player-1[1]: Enter the row,column; eg. 1,2: ")
        p1_loc=p1_loc.split(",")
        p1_row=int(p1_loc[0]); p1_row=p1_row-1;
        p1_col=int(p1_loc[1]); p1_col=p1_col-1;
        print(p1_row)
        print(p1_col)
        
        if init_arr[p1_row][p1_col] == 0:
            #Modify Array
            init_arr[p1_row][p1_col]=1
            print(init_arr)
        else:
            print(f"Oops!! Row,Column: {p1_row, p1_col} is already used, please use different place")
        
        res=check_result(init_arr, row, column)
        if res == 1 or res == 2:
            if res == 1:
                print("Player#1 is the winner of this game!!!")
                return flag
            elif res == 2:
                print("Player#2 is the winner of this game!!!")
                return flag
        else:
            print("No Winner Yet!!! Continue playing!!")
            pass 
        
        #If Matrix is full, return the control to while
        nz = np.count_nonzero(init_arr)
        if nz == count:
            continue
        
        #Start The Game
        p2_loc=input("Player-2[2]: Enter the row,column; eg. 1,2: ")
        p2_loc=p2_loc.split(",")
        p2_row=int(p2_loc[0]); p2_row=p2_row-1;
        p2_col=int(p2_loc[1]); p2_col=p2_col-1;
        
        
        print(p2_row)
        print(p2_col)
        
        if init_arr[p2_row][p2_col] == 0:
            #Modify Array
            init_arr[p2_row][p2_col]=2
            print(init_arr)
        else:
            print(f"Opps!!! Row,Column: {p2_row, p2_col} is already used, please use different place")
        
        #Check non-zero elements in array
        nz = np.count_nonzero(init_arr)
        #Check Matrix and Declare result
        res=check_result(init_arr, row, column)
        if res == 1 or res == 2:
            if res == 1:
                print("Player#1 is the winner of this game!!!")
                return flag
            elif res == 2:
                print("Player#2 is the winner of this game!!!")
                return flag
        else:
            print("No Winner Yet!!! Continue playing!!")
            pass 
        
    #Check Matrix and Declare result after all the places are occupied 
    res=check_result(init_arr, row, column)
    if res == 1 or res == 2:
        if res == 1:
            print("Player#1 is the winner of this game!!!")
            return flag
        elif res == 2:
            print("Player#2 is the winner of this game!!!")
            return flag
    else:
        print("No Winner :( ... Restart The Game.......")
        return flag    
#    return init_arr
    return flag

def check_result(arr_val, row, column):
    #global row
    #global column
    
    row=row-1
    column=column-1
    flag=0
    #initialize list to store and comare result
    arr_res=[]
    c1=row
    c2=column
    
    #Check the match in vertical
    while c2 >= 0:
        c1=row
        while c1 >= 0:
            #print(f"inside the vertical scanning function")
            #print(f"inside the loop; value of c1 {c1}")
            #print(f"inside the loop; value of c2 {c2}")
            arr_res.append(arr_val[c1][c2])
            #print(f"inside the loop(v); value of arr_res {arr_res}")
                    
            if arr_res.count(1) == row+1:
                #print(f"Player 1 Wins!! and Final result is \n {arr_val}") 
                flag=1
                return flag
            elif arr_res.count(2) == row+1:
                #print(f"Player 2 Wins!! and Final result is \n {arr_val}")
                flag=2
                return flag
            else:
                pass
                #print("No Winner Yet!!")
            c1=c1-1
        arr_res=[]
        c2=c2-1

    #initialize list to store and comare result
    arr_res=[]
    c1=row
    c2=column
    
    #Check the match in horizontal
    while c1 >= 0:
        c2=row
        while c2 >= 0:
            #print(f"inside the horizontal scanning function")
            #print(f"inside the loop; value of c1 {c1}")
            #print(f"inside the loop; value of c2 {c2}")
            arr_res.append(arr_val[c1][c2])
            #print(f"inside the loop(h); value of arr_res {arr_res}")
                    
            if arr_res.count(1) == row+1:
                #print(f"Player 1 Wins!! and Final result is \n {arr_val}") 
                flag=1
                return flag
            elif arr_res.count(2) == row+1:
                #print(f"Player 2 Wins!! and Final result is \n {arr_val}")
                flag=2
                return flag
            else:
                pass
                #print("No Winner Yet!!")
            c2=c2-1
        arr_res=[]
        c1=c1-1
        
    #initialize list to store and comare result
    arr_res=[]
    c1=row
    
    #Check the match in diagonal(1)
    while c1 >= 0:
        #print(f"inside the diagonal scanning function")
        #print(f"inside the loop; value of c1 {c1}")
        arr_res.append(arr_val[c1][c1])
        #print(f"inside the loop(d1); value of arr_res {arr_res}")
                
        if arr_res.count(1) == row+1:
            #print(f"Player 1 Wins!! and Final result is \n {arr_val}") 
            flag=1
            return flag
        elif arr_res.count(2) == row+1:
            #print(f"Player 2 Wins!! and Final result is \n {arr_val}")   
            flag=2
            return flag
        else:
            pass
            #print("No Winner!!")
        c1=c1-1

    #initialize list to store and comare result
    arr_res=[]
    c1=row
    c2=0
    #Check the match in diagonal(2)
    while c1 >= 0 and c2 <= column:
        #print(f"inside the loop; value of c1 {c1}")
        #print(f"inside the loop; value of c2 {c2}")
        arr_res.append(arr_val[c1][c2])
        #print(f"inside the loop(d2); value of arr_res {arr_res}")
                
        if arr_res.count(1) == row+1:
            #print(f"Player 1 Wins!! and Final result is \n {arr_val}")   
            flag=1
            return flag
        elif arr_res.count(2) == row+1:
            #print(f"Player 2 Wins!! and Final result is \n {arr_val}") 
            flag=2
            return flag
        else:
            pass
            #print("No Winner!!")
        c1=c1-1
        c2=c2+1
    
    return flag

play_game()

#def declare_result():
        
#    ret_val=play_game()
    
    #check_result(ret_val)            
#    if ret_val == 1:
        #Process the result
#        ret_val1=check_result()
#        if ret_val1 == 1:
#            print("Player#1 is the winner of this game!!!")
#        elif ret_val1 == 2:
#            print("Player#2 is the winner of this game!!!")
#        else:
#            print("There is no winner of this game...try again!!")
#    else:
#        print("Program Aborted!! User might have entered incorrect input...")

#Run the program
#declare_result()