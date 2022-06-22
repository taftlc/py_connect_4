#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Script: connect_4.py
    Desc:  Generate game of connect 4 in console
    Author: Taft, Luke C. 40498618
    Last Modified: 21, June 2022
"""


#x = horizantal axis
#y = vertical axis
     
def make_pb():
    playing_board=[[" ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " "]
                   ] 
    return playing_board

def print_pb(playing_board):

    #test pieces for the board
    playing_board[0][1] = "X"
    playing_board[5][5] = "O"
    
    
    #header containing orientation numbers
    header_nums = " "
    for num in range(0, len(playing_board)):
        header_nums += "  "+ str(num) +"   "
    print(header_nums)
    print ("|-----" * (len(playing_board)) + "|")
    
    #printing rows
    for row in range(len(playing_board[0])):
        print("|     " * (len(playing_board) +1))
        
        active_row = ""
        for column in range(len(playing_board)):
            active_row += ("|  "+str(playing_board[column][row])) + "  "
        print(active_row + "| " + str(row))
    
        print("|     " * (len(playing_board) +1))
        
        print ("|-----" * (len(playing_board)) + "|")
        
def move_checker(playing_board, move):
    #error checking for the column existing
    if move < 1 or move > (len(playing_board)):
        return False
   
    #error checking for the column being full
    if playing_board[move-1][0] != " ":
        return False
    
    return True

def select_space(playing_board, column, player):
    #throw it to the move_checker
    if not move_checker(playing_board, column):
        print("Moving an " + player + " piece in column " +str(column))
        print("Make sure to pick a column between 0 and " + str(len(playing_board) - 1) + " that is not full \n")
        return False
    
    
        
        
    

playing_board = make_pb()
print_pb(playing_board)