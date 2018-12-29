#TIC TAC TOE (EXTENDED AI OPTIMIZATION)
#Using Loops & Functions & Lists

#STAGE 1:
#Create the main loop
#Print the board
#Create your loop
#Get the user input
#Put the user input in the board

#STAGE 2:
#Check for player win (8 possibilities)

#STAGE 3:
#Create the Second player (HUMAN)
#Check for the second player win
#Check for a full board (TIE)

#STAGE 4:
#Combine STAGE 2 & STAGE 3 into one function
#def is_winner(board, player):
#Create a function to check if the board is full
#def is_board_full(board)

#STAGE 5:
#Creating our game AI
#def get_computer_move(board, player)
#i)return random number
#ii)make sure the random number is for an empty spot

#import
import os
import time 
import random

#Define the board
board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

#Print the header
def print_header():
    print("""
                     TIC TOC TOE       
        To Play Tic-Tac-Toe, you need to get three in a row .....
        Your choices are defined, they must be from 1 to 9  ..... """)

#define the print_board function
def print_board():
    print("   |   |   ")
    print(" "+board[1]+" | "+board[2]+" | "+board[3]+" | ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" "+board[4]+" | "+board[5]+" | "+board[6]+" | ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" "+board[7]+" | "+board[8]+" | "+board[9]+" | ")
    print("   |   |   ")

def is_winner(board, player):
    if  (board[1] == player and board[2] == player and board[3] == player) or \
        (board[4] == player and board[5] == player and board[6] == player) or \
        (board[7] == player and board[8] == player and board[9] == player) or \
        (board[1] == player and board[4] == player and board[7] == player) or \
        (board[2] == player and board[5] == player and board[8] == player) or \
        (board[3] == player and board[6] == player and board[9] == player) or \
        (board[1] == player and board[5] == player and board[9] == player) or \
        (board[3] == player and board[5] == player and board[7] == player) :
        return True
    else:
        return False

def is_board_full(board):
    if " " in board:
        return False
    else:
        return True

def get_computer_move(board, player):
    #check for win
    for i in range(1, 10):
        if board[i] == " ":
            board[i] = player
            if is_winner(board, player):
                return i
            else:
                board[i] = " "

    ''' baddd logic
    #Check columns for a win
    for i in [1,2,3]:
        if board[i] == player and board[i+3] == player and board[i+6] == " ":
            return i+6
        if board[i+3] == player and board[i+6] == player and board[i] == " ":
            return i
        if board[i] == player and board[i+6] == player and board[i+3] == " ":
            return i+3
        '''

    #if the center square is empty choose that
    if board[5] == " ":
        return 5
    
    while True:
        move = random.randint(1,9)
        #if the move is blank, go ahead and return otherwise try again
        if board[move] == " ":
            return move
            break
            
    return 5         


while True:
    os.system("clear")
    print_header()
    print_board()

    #get player X input
    choice = int(input("Please choose any space for X "))

    #check to see if the space is empty first
    if board[choice] == " ":
        board[choice] = "X"
    else:
        print("Sorry, that space is not Empty !! ")
        time.sleep(1)

    #STAGE 2:
    #Check for player win (8 possibilities)
    #check for X win

    if is_winner(board, "X"):
        os.system("clear")
        print_header()
        print_board()
        print("X Wins! , Conguralutions !!!")
        break

    #If the Board is full, do something
    if is_board_full(board):
        print_board()
        print("Tie!!!")
        break

    
    os.system("clear")
    print_header()
    print_board()

    #get player O input
    choice = get_computer_move(board, "O")

    #check to see if the space is empty first
    if board[choice] == " ":
        board[choice] = "O"
    else:
        print("Sorry, that space is not Empty !! ")
        time.sleep(1)

    #STAGE 2:
    #Check for player win (8 possibilities)
    #check for O win
    if is_winner(board, "O"):
        os.system("clear")
        print_header()
        print_board()
        print("O Wins! , Conguralutions !!!")
        break

    #If the Board is full, do something
    if is_board_full(board):
        print_board()
        print("Tie!!!")
        break