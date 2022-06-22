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


playing_board = make_pb()
print_pb(playing_board)