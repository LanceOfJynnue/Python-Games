import random
import os
import sys

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_board(checkBoard):
    print("Current board status:")
    print("+---+---+---+")
    for row in checkBoard:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print("\n+---+---+---+")
    print("** \"X\" is the Computer.")
    print("** \"O\" is You, the Player.")

def make_list_of_free_fields(checkBoard,printRes=True):
    print("Free Field: ",end="")
    checkCell = 0
    availCells = False
    for i in range(len(checkBoard)):
        for j in range(len(checkBoard[i])):
            checkCell += 1
            if checkBoard[i][j] not in ["X", "O"]:
                if availCells == False:
                    if printRes == True:
                        print(checkCell,end="")
                    availCells = [checkCell]
                else:
                    if printRes == True:
                        print(",",checkCell,end="")
                    availCells.append(checkCell)
    return availCells

def victory_for(checkBoard, sign):
    if sign == 1: check = "O"
    else: check = "X"
    playing = True
    
    selCells = make_list_of_free_fields(checkBoard,printRes=False)
    
    for i in range(len(checkBoard)):
        checkRow = 0
        for j in range(len(checkBoard[i])):
            if checkBoard[i][j] == check:
                checkRow += 1
        if checkRow == 3: playing = False
    
    for i in range(len(checkBoard)):
        checkCol = 0
        for j in range(len(checkBoard[i])):
            if checkBoard[j][i] == check:
                checkCol += 1
        if checkCol == 3: playing = False
    
    checkDia = 0
    
    for i in range(len(checkBoard)):
        if checkBoard[i][i] == check:
            checkDia += 1
        if checkDia == 3: playing = False
    
    checkDia = 0
    dia = 2
    
    for i in range(len(checkBoard)):
        if checkBoard[i][dia] == check:
            checkDia += 1
        if checkDia == 3: playing = False
        dia -= 1
    
    if playing == False:
        if check == "O":
            clear_terminal()
            display_board(board)
            print("\n'O' WON!")
        elif check == "X":
            clear_terminal()
            display_board(board)
            print("\n'X' WON!")
    elif selCells == False:
        clear_terminal()
        display_board(board)
        playing = False
        print("\nIT'S A DRAW.")
    
    return playing

def player_move(checkBoard, selectionCells, sign):
    choiceCell = input("\nInput the cell number for your turn: ")
    while True:
        while True:
            try:
                choiceCell = int(choiceCell)
                break
            except:
                choiceCell = input("Invalid input. Try again: ")
        if choiceCell in selectionCells: break
        else: choiceCell = input("That cell is not available. Try again: ")
    for i in range(len(checkBoard)):
        for j in range(len(checkBoard[i])):
            if  choiceCell == checkBoard[i][j]:
                checkBoard[i][j] = sign
                return checkBoard

def enemy_move(checkBoard, selectionCells):
    enemy_choice = random.randint(0,len(selectionCells)-1)
    enemy_cell = enemy_choice+1
    for i in range(3):
        for j in range(3):
            if selectionCells[enemy_choice] == checkBoard[i][j]:
                checkBoard[i][j] = "X"
                result = [enemy_cell, checkBoard]
                return result

clear_terminal()

print("Welcome to Tic-Tac-Toe! Select the number of your choice.")
print("1. Single Player")
print("2. Two Player")
print("[Other Input] EXIT")

try:
    mode = int(input("\n"))
except:
    sys.exit()

if mode == 1:
    multiplayer = False
elif mode == 2:
    multiplayer = True
else: sys.exit()

clear_terminal()

player_turn = random.randint(0,1)

while True:
    board = [[0 for row in range(3)] for col in range(3)]
    x = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            x += 1
            board[i][j] = x
    playing = True
    enemy_cell = False
    while playing == True:
        clear_terminal()
        if enemy_cell != False:
            print(f"The Computer played: {enemy_cell}\n")
        display_board(board)
        selectionCells = make_list_of_free_fields(board)
        if playing == True:
            if player_turn == 1:
                print("\n\n['O' TURN]")
                sign = "O"
                board = player_move(board,selectionCells,sign)
                playing = victory_for(board,player_turn)
                player_turn = 0
            else:
                print("\n\n['X' TURN]")
                sign = "X"
                if multiplayer == True:
                    board = player_move(board,selectionCells,sign)
                elif multiplayer == False:
                    enemy_cell, board = enemy_move(board,selectionCells)
                playing = victory_for(board,player_turn)
                player_turn = 1
    choice = input("\nEnter 'Y' if you wish to play again.\n")
    if choice == "Y": continue
    else: 
        print(input("THANKS FOR PLAYING!"))
        break
    
